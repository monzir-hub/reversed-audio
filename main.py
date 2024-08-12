import scipy.io.wavfile as wave
import numpy as np

# Read the WAV file
samplerate, data = wave.read('test.wav')

# Calculate length of audio file in seconds
length_seconds = len(data) / samplerate

# Calculate number of samples in the file
num_samples = len(data)

# Calculate data size in bytes (including header)
data_size_bytes = num_samples * data.itemsize

# Calculate data size in bits
data_size_bits = data_size_bytes * 8

# Calculate bit rate (bits per sample)
bits_per_sample = data.itemsize * 8

# Determine type of recording
type_of_recording = 'stereo' if data.ndim > 1 and data.shape[1] == 2 else 'mono'

# Sampling rate
sampling_rate = samplerate

# Reverse the audio
reversed_data = np.flipud(data)

# Write the reversed audio to a new file
wave.write('reversed_test.wav', samplerate, reversed_data)

# Output the calculated properties
print("Length of audio file:", length_seconds, "seconds")
print("Data Size:", data_size_bytes, "bytes")
print("Audio Format:")
print("  - Encoding: PCM")
print("  - Sampling Rate:", sampling_rate, "Hz")
print("  - Bits Per Sample:", bits_per_sample, "bits")
print("  - Type of Recording:", type_of_recording)

print("Audio reversed and saved as 'reversed_test.wav'")
