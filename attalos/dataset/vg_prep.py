from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import zipfile
from collections import defaultdict
from dataset_prep import DatasetPrep, RecordMetadata, SplitType


VISUAL_GENOME_IMAGES = 'https://visualgenome.org/static/data/dataset/image_data.json.zip'
VISUAL_GENOME_METADATA = 'https://visualgenome.org/static/data/dataset/image_data.json.zip'
VISUAL_GENOME_REGIONS = 'https://visualgenome.org/static/data/dataset/region_descriptions.json.zip'
VISUAL_GENOME_OBJECTS = 'https://visualgenome.org/static/data/dataset/objects.json.zip'
VISUAL_GENOME_ATTRIBUTES = 'https://visualgenome.org/static/data/dataset/attributes.json.zip'
VISUAL_GENOME_RELATIONSHIPS = 'https://visualgenome.org/static/data/dataset/relationships.json.zip'



class MSCOCODatasetPrep(DatasetPrep):
    def __init__(self, dataset_directory, split='train'):
        """
        Initialize MS COCO specific dataset prep iterator
        Args:
            dataset_directory: Directory to store image files in
            split: Train/Val split is allowed
        Returns:

        """
        super(MSCOCODatasetPrep, self).__init__('MS COCO', dataset_directory)
        if split.lower() == 'train':
            self.split = SplitType.TRAIN
        elif split.lower() == 'test':
            raise NotImplementedError('Split type not yet implemented')
        elif split.lower() == 'val':
            raise NotImplementedError('Split type not yet implemented')
        else:
            raise NotImplementedError('Split type not yet implemented')
        self.instances_filename = self.get_candidate_filename(VISUAL_GENOME_RELATIONSHIPS)
        self.caption_filename = self.get_candidate_filename(VISUAL_GENOME_METADATA)
        self.image_filename = self.get_candidate_filename(TRAIN_IMAGES_URL)
        self.download_dataset()
        self.item_info = self.load_metadata()
        self.image_file_handle = None

    def download_dataset(self):
        """
        Downloads the dataset if it's not already present in the download directory
        Returns:

        """
        self.download_if_not_present(self.instances_filename, VISUAL_GENOME_RELATIONSHIPS)
        self.download_if_not_present(self.caption_filename, VISUAL_GENOME_METADATA)
        self.image_filename = self.get_candidate_filename(TRAIN_IMAGES_URL)

    def load_metadata(self):
        """
        Load the MS COCO dataset to allow for efficient iteration
        Returns:

        """
        if self.split == SplitType.TRAIN:
            split_name = 'train'
        elif self.split == SplitType.VAL:
            split_name = 'val'
        else:
            raise NotImplementedError('Split type not yet implemented')

	raise NotImplementedError('Split type not yet implemented')

    def get_key(self, key):
        """
        Return metadata about key
        Args:
            key: ID who's metadata we'd like to extract

        Returns:
            RecordMetadata: Returns ParserMetadata object containing metadata about item
        """
        item = self.item_info[key]
        return RecordMetadata(id=key, image_name=item['fname'], tags=item['tags'], captions=item['captions'])

    def extract_image_by_key(self, key):
        """
        Return an image based on the input key
        Args:
            key: ID of the file we'd like to extract

        Returns:
            Image Blob: Bytes of the image associated with the input ID
        """
	NotImplementedError('Split type not yet implemented')

    def extract_image_to_location(self, key, desired_file_path):
        """
        Write image based on the input key to the desired location
        Args:
            key: ID of the file we'd like to extract
            desired_file_path: Output filename that we should write the file to

        Returns:

        """
	raise NotImplementedError('Split type not yet implemented')

    def __iter__(self):
        """
        Iterator over the dataset.
        Returns:
            RecordMetadata: Information about the next key
        """
        for key in sorted(self.list_keys()):
            yield self.get_key(key)

        raise StopIteration()

    def list_keys(self):
        """
        List all keys in the dataset
        Returns:

        """
        return self.item_info.keys()
