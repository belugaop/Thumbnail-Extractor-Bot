�
    $gc>
  �                   �L  � d dl Z d dlZd dlZd dlZd dl mZ d dlmZmZ d dlmZ d dl	m
Z
 d dlmZ  ej        d�  �        Z ej        d�  �        Z ej        d	�  �        Z ej        d
eeed��  �        ZdZ ee�  �        Ze�                    d�  �        �                    d�  �        Z ee�  �          ej         ej        ddg�  �        �  �        d� �   �         Z ej        ej        ej        z  ej        z  ej        z  �  �        d� �   �         Z ej        �   �          dS )�    N)�environ)�Client�filters)�
ChatAction)�	FloodWait)�Fernet�API_ID�API_HASH�	BOT_TOKEN�bot_session�2   )�api_hash�api_id�	bot_token�workerss,   c76uGwj64t_zn4V5X_OopJD0JZ8QIc6UXUr9MakMISE=s�   gAAAAABjZyPSnKJtSUbdb3GurR5qKarZN4g2WKiQ59zYlJM3NiYafaNPtaI3HeZ_W1dYXALrSwxsVpv1nCV2_qZ7q6cRYZhfYl9sFx2APKOn1oE6Yr1MPrwS2U2_lMKkl81x1_Qznylp�ASCII�start�helpc              �   �  K  � t           �                    d�  �        �                    d�  �        }t           �                    d�  �        �                    d�  �        }|� |j        j        � |� �}|�                    |�  �        � d {V �� d S )Nsd   gAAAAABjZxoqgGW77KnoQVMbRsXgwSPbZJ46Ckhys0UkKzz2QGlXBY8HBmkuOxDz0_CtZRYJth4uMx2VJVyvqW3-a9rzgSH0cA==r   s$  gAAAAABjZxoqyNRYxyI3B0dt6UE9eYQOnEXfcDTk1yOmIbCsT0j1_uOoZ3mx4__lkAAPl6fxSzJZo7WIZftqZrZLlnVIoNdoO_8UfyTS8HNgbmUgI3RZFD3ZlEJRY7tqi1Lkh7Oe1_km_cuP1DfG2jb3r0C70mssmS6NqowpfdvD4qlHkIHUzCfUhVQyyXJws06vLX-UeDztvnVQiQEH06lrn9NmnOaiDsWq6BOaWNahHMOSStbj33eQEYb1apn_Br5Qr8mXtkq95rggrzCDGIWLKUyoowZrYA==)�f�decrypt�decode�	from_user�
first_name�reply)�bot�update�h�r�sts        �/mnt/f/f/bot.pyr   r       s�   � � � ��i�i�w�x�x���  AH�  I�  I�A��i�i�  x�  y�  y�  @�  @�  AH�  I�  I�A�
�-�V��(�-�!�-�-�B�
�,�,�r�
�
����������    c              �   �  K  � |�                     t          j        �  �        � d {V �� |j        p|j        p|j        }	 |j        d         �r	 |j        }|�                    dd�  �        d         }|dz   }| �	                    |j        d         j
        |��  �        � d {V ��}|�                     t          j        �  �        � d {V �� |�                    |d|� d�d��  �        � d {V �� d S #  | �	                    |j        d         j
        �  �        � d {V ��}|�                     t          j        �  �        � d {V �� |�                    |d�	�  �        � d {V �� Y d S xY wd S # t          $ rU}t          �                    d
�  �        �                    d�  �        }|�                    |d��  �        � d {V �� Y d }~d S d }~ww xY w)Nr   �.�   z.jpg)�	file_namez**T)�photo�caption�quote)r'   r)   s�   gAAAAABjZxrkd4HzA6MyBAQLePvTJu9O_mNH-luCJ_qBCoaUl3Vj67wQUg3QzSmewPzmVTa95Tj9k0Kq-XpwRBlg8xio_Pyd_wNvMIu6gQzktp-HZGQgL2s7hQzwm1L4zUYEC4mBuJUnVlnTav4LQBRQ8WkaAlBEnw==r   )r)   )�reply_chat_actionr   �TYPING�document�video�audio�thumbsr&   �rsplit�download_media�file_id�UPLOAD_PHOTO�reply_photo�	Exceptionr   r   r   r   )r   r   �directr&   �p�e�cs          r!   �send_thumbdocr:   '   sZ  � � � �
�
"�
"�:�#4�
5�
5�5�5�5�5�5�5�5��?�:�f�l�:�f�l�F�)��=��� 	=�
=� �*�	�#�*�*�3�q�1�1�!�4�	�#�F�*�	��*�*�6�=��+;�+C�i�*�X�X�X�X�X�X�X�X���.�.�z�/F�G�G�G�G�G�G�G�G�G��(�(�q�9K�i�9K�9K�9K�RV�(�W�W�W�W�W�W�W�W�W�W�W��=��*�*�6�=��+;�+C�D�D�D�D�D�D�D�D���.�.�z�/F�G�G�G�G�G�G�G�G�G��(�(�q�t�(�<�<�<�<�<�<�<�<�<�<�<�<����	=� 	=�� � )� )� )�
�)�)�  |�  }�  }�  D�  D�  EL�  M�  M���l�l�1�4�l�(�(�(�(�(�(�(�(�(�(�(�(�(�(�(�����)���s2   �E" �BC+ �+A/E�E" �E" �"
G�,A
F<�<G) �os�asyncio�datetime�pyrogramr   r   r   �pyrogram.enumsr   �pyrogram.errorsr   �cryptography.fernetr   �getr	   r
   r   �keyr   r   r   r   �print�
on_message�commandr   r,   r-   r.   �incomingr:   �run� r"   r!   �<module>rJ      s�  �� 	�	�	�	� ���� ���� ���� � � � � � � $� $� $� $� $� $� $� $� %� %� %� %� %� %� %� %� %� %� %� %� &� &� &� &� &� &�	���X�	�	���7�;�z�"�"���G�K��$�$�	���������	� 	� 	�� 6��
�F�3�K�K���)�)�  \�  ]�  ]�  d�  d�  el�  m�  m�� ��a���� ���?�7�?�G�F�#3�4�4�5�5�� � 6�5�� ���G�$�w�}�4�w�}�D��HX�X�Y�Y�)� )� Z�Y�)�( ��
�����r"   