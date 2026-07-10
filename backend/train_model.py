"""
Scalp Disease Detection - Model Training
Trains MobileNetV2 (transfer learning) + Custom CNN on 14 disease classes.
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models, callbacks
from tensorflow.keras.applications import MobileNetV2
from sklearn.utils.class_weight import compute_class_weight

# ── Config ──────────────────────────────────────────────────────────────────
DATASET_DIR = os.path.join(os.path.dirname(__file__), '..', 'all')
IMG_SIZE    = 224
BATCH_SIZE  = 16
EPOCHS_CNN  = 30
EPOCHS_MN   = 20
NUM_CLASSES = 14
SEED        = 42

CLASSES = [
    'acne-keloidalis', 'alopecia-areata', 'androgenic-alopecia',
    'discoid-lupus', 'dissecting-cellulitis', 'folliculitis-decalvans',
    'hirsutism', 'hot-comb-alopecia', 'lichen-planopilaris',
    'pseudopelade', 'telogen-effluvium', 'trichorrhexis-nodosa',
    'trichotillomania', 'tufted-folliculitis'
]

os.makedirs(os.path.join(os.path.dirname(__file__), 'models'), exist_ok=True)

# ── Data Augmentation ────────────────────────────────────────────────────────
data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal_and_vertical"),
    layers.RandomRotation(0.3),
    layers.RandomZoom(0.2),
    layers.RandomBrightness(0.2),
    layers.RandomContrast(0.2),
])

# ── Load Dataset ─────────────────────────────────────────────────────────────
def load_datasets():
    train_ds = tf.keras.utils.image_dataset_from_directory(
        DATASET_DIR, validation_split=0.2, subset="training",
        seed=SEED, image_size=(IMG_SIZE, IMG_SIZE), batch_size=BATCH_SIZE,
        class_names=CLASSES, label_mode='categorical'
    )
    val_ds = tf.keras.utils.image_dataset_from_directory(
        DATASET_DIR, validation_split=0.2, subset="validation",
        seed=SEED, image_size=(IMG_SIZE, IMG_SIZE), batch_size=BATCH_SIZE,
        class_names=CLASSES, label_mode='categorical'
    )
    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.map(lambda x, y: (data_augmentation(x, training=True), y),
                            num_parallel_calls=AUTOTUNE).prefetch(AUTOTUNE)
    val_ds   = val_ds.prefetch(AUTOTUNE)
    return train_ds, val_ds

# ── MobileNetV2 Model ────────────────────────────────────────────────────────
def build_mobilenet():
    base = MobileNetV2(input_shape=(IMG_SIZE, IMG_SIZE, 3),
                       include_top=False, weights='imagenet')
    # Freeze base, unfreeze last 30 layers
    base.trainable = True
    for layer in base.layers[:-30]:
        layer.trainable = False

    inputs = tf.keras.Input(shape=(IMG_SIZE, IMG_SIZE, 3))
    x = tf.keras.applications.mobilenet_v2.preprocess_input(inputs)
    x = base(x, training=False)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dense(512, activation='relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.4)(x)
    x = layers.Dense(256, activation='relu')(x)
    x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(NUM_CLASSES, activation='softmax')(x)
    model = tf.keras.Model(inputs, outputs, name='MobileNetV2_Scalp')
    model.compile(
        optimizer=tf.keras.optimizers.Adam(1e-4),
        loss='categorical_crossentropy',
        metrics=['accuracy', tf.keras.metrics.AUC(name='auc')]
    )
    return model

# ── Custom CNN Model ──────────────────────────────────────────────────────────
def build_cnn():
    model = models.Sequential(name='CustomCNN_Scalp')
    model.add(layers.Input(shape=(IMG_SIZE, IMG_SIZE, 3)))
    model.add(layers.Rescaling(1./255))

    for filters in [32, 64, 128, 256, 512]:
        model.add(layers.Conv2D(filters, 3, padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.Conv2D(filters, 3, padding='same', activation='relu'))
        model.add(layers.BatchNormalization())
        model.add(layers.MaxPooling2D(2))
        model.add(layers.Dropout(0.25))

    model.add(layers.GlobalAveragePooling2D())
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dropout(0.3))
    model.add(layers.Dense(NUM_CLASSES, activation='softmax'))

    model.compile(
        optimizer=tf.keras.optimizers.Adam(1e-3),
        loss='categorical_crossentropy',
        metrics=['accuracy', tf.keras.metrics.AUC(name='auc')]
    )
    return model

# ── Training Callbacks ────────────────────────────────────────────────────────
def get_callbacks(model_name):
    model_path = os.path.join(os.path.dirname(__file__), 'models', f'{model_name}.h5')
    return [
        callbacks.ModelCheckpoint(model_path, save_best_only=True,
                                  monitor='val_accuracy', verbose=1),
        callbacks.EarlyStopping(monitor='val_accuracy', patience=8,
                                restore_best_weights=True, verbose=1),
        callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.3,
                                    patience=4, min_lr=1e-7, verbose=1),
        callbacks.TensorBoard(log_dir=os.path.join(
            os.path.dirname(__file__), 'logs', model_name))
    ]

# ── Plot Training History ────────────────────────────────────────────────────
def plot_history(history, model_name):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    axes[0].plot(history.history['accuracy'], label='Train Acc')
    axes[0].plot(history.history['val_accuracy'], label='Val Acc')
    axes[0].set_title(f'{model_name} - Accuracy')
    axes[0].legend()
    axes[1].plot(history.history['loss'], label='Train Loss')
    axes[1].plot(history.history['val_loss'], label='Val Loss')
    axes[1].set_title(f'{model_name} - Loss')
    axes[1].legend()
    plt.tight_layout()
    plot_path = os.path.join(os.path.dirname(__file__), 'models', f'{model_name}_history.png')
    plt.savefig(plot_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"[✓] Training plot saved: {plot_path}")

# ── Main ─────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print("=" * 60)
    print("  SCALP DISEASE DETECTION — MODEL TRAINING")
    print("=" * 60)
    print(f"[✓] TensorFlow version: {tf.__version__}")
    print(f"[✓] GPU available: {len(tf.config.list_physical_devices('GPU')) > 0}")
    print(f"[✓] Dataset: {DATASET_DIR}")
    print(f"[✓] Classes: {NUM_CLASSES}")

    train_ds, val_ds = load_datasets()
    print(f"[✓] Dataset loaded successfully")

    # ── Train Custom CNN ──
    print("\n[1/2] Training Custom CNN...")
    cnn_model = build_cnn()
    cnn_model.summary()
    cnn_history = cnn_model.fit(
        train_ds, validation_data=val_ds,
        epochs=EPOCHS_CNN, callbacks=get_callbacks('cnn_model'), verbose=1
    )
    plot_history(cnn_history, 'cnn_model')
    cnn_val_acc = max(cnn_history.history['val_accuracy'])
    print(f"[✓] CNN Best Val Accuracy: {cnn_val_acc:.4f}")

    # ── Train MobileNetV2 ──
    print("\n[2/2] Training MobileNetV2...")
    mn_model = build_mobilenet()
    mn_model.summary()
    mn_history = mn_model.fit(
        train_ds, validation_data=val_ds,
        epochs=EPOCHS_MN, callbacks=get_callbacks('mobilenet_model'), verbose=1
    )
    plot_history(mn_history, 'mobilenet_model')
    mn_val_acc = max(mn_history.history['val_accuracy'])
    print(f"[✓] MobileNetV2 Best Val Accuracy: {mn_val_acc:.4f}")

    print("\n" + "=" * 60)
    print("  TRAINING COMPLETE")
    print(f"  CNN Accuracy:        {cnn_val_acc*100:.2f}%")
    print(f"  MobileNetV2 Accuracy:{mn_val_acc*100:.2f}%")
    print("  Models saved in backend/models/")
    print("=" * 60)
