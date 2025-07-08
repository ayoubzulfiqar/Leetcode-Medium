import pandas as pd
import numpy as np

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(signups, confirmations, on='user_id', how='left')
    
    merged_df['is_confirmed'] = (merged_df['action'] == 'confirmed').astype(int)
    
    confirmation_stats = merged_df.groupby('user_id').agg(
        confirmed_count=('is_confirmed', 'sum'),
        total_requests=('action', 'count')
    ).reset_index()
    
    confirmation_stats['confirmation_rate'] = np.where(
        confirmation_stats['total_requests'] == 0,
        0.00,
        confirmation_stats['confirmed_count'] / confirmation_stats['total_requests']
    )
    
    confirmation_stats['confirmation_rate'] = confirmation_stats['confirmation_rate'].round(2)
    
    return confirmation_stats[['user_id', 'confirmation_rate']]