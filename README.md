# DataProcessor

## Usage

```python
from data_processor import DataProcessor

processor = DataProcessor()
processor.load_data('data.csv')
processor.filter_data(lambda row: int(row['age']) > 25)
processor.sort_data('name')
print(processor.calculate_mean('salary'))
processor.save_data('processed_data.csv')
```
