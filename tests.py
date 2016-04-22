from unittest import TestCase
from unittest.mock import MagicMock

from rest_framework import serializers

from django_rest_framework_base64_fields import Base64FileField


class MainTestCase(TestCase):
    def setUp(self):
        self.encoded_file = """data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAwACkDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+vO/ib8UoPAYt7G2tVu9WuU8xI3bakSZIDNjk5IIAHoeRgZ9EryDxktxpnxTlnWO0+z6jpsCyy3SKweNJiJbcBs8OpXJ7ZH1pSkoq7Gk27IyfC/x6vZ9Wgt/Eum2sFnO/li6tQyiI8ZJDE7gMjOCCAc89D7rXzN40Wa0+HY0oavBfRWhhIi8tVCMHfdIuMkSMZQCCfuq55zhfojw/cfbPDel3O/f51pFJuznOUBzU06kaivB3Q5RcXaRo0UUVZIjMqIXdgqqMkk4AFePeE4IPij4417xReiSTRbMf2bpkYZlDDhmfggg4wcEf8tMH7tbvxt1qXR/htcxwMUfUZksi4PRWyz/AJqrL/wKrnwgi0+D4badHp8iuA0hmxjcshckhvcAr9RtPQik0nowTsJ4m+Gml6n4O1DS7CELfSIGguJnLMJFO5Rk/dUkYOB0OeTXnHwa8eXGi6j/AMIfrqSRQy3DQ2jS5Bt584aFgemW6ejHHO7j6Br5e+LDQw+O/FEUR8pg1vPHsOD53lJyMdDhmJ96FFJWQ223dn1DRVTSrpr7R7K7fG6e3jlOPVlB/rVumI8/8b3UWqXn9kXFpBJBaSJLieMPvfbwQDxgBj+NYHhXTYdF8bJqdtqUmn2EyFLmwSIeTK2CFJORtAJB6HHOCAxrtdf8JzanqL31rcxq7qAY5QcZHGQw6DpxisGLwvrhu1ha1CITgzmRWRR64B3H6YGfbqPJq/WoVnKKbX4WO6HsZU7M7nWr5NO0S8vGmSIxxHY7kAbzwg57liAB3JArwfX/AAc/iDxEdQuL8fY5ijTxbP3p2jGA/o3c9cnvgV6VdfCfSLwxtcatrkzwuJYvNvNyRyDkMqbdowewAFTad4JuvPH9pTwiBD923ZiZB7kgbfwyfcda6MTGu5xdLtYxpOnytTNHwZfGXTTp5TBswArD7uwk7VHptAxj0ArpqitrWCzhENtCkUY6KgwPr9alrqowlCCjJ3aMpyUpNo//2Q=="""
        self.base64_file_field = Base64FileField()

    def test_FileField_to_internal_value(self):
        content_file = self.base64_file_field.to_internal_value(self.encoded_file)
        self.assertEqual(content_file.size, 1375)
        self.assertEqual(content_file.name.split('.')[-1], 'jpg')

    def test_FileField_to_representation(self):
        fieldFile = MagicMock()
        fieldFile.url = 'test.url'
        representation = self.base64_file_field.to_representation(fieldFile)
        self.assertEqual(representation, fieldFile.url)

    def test_incorrect_type_not_string(self):
        with self.assertRaises(serializers.ValidationError):
            self.base64_file_field.to_internal_value({})  # dict is incorrect
