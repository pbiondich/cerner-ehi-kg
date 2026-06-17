# UCM_POSITION_MAP_CELL

> Stores the details for each cell in the position map for a protocol batch.

**Description:** Unified Case Manager - Position Map Cell  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CELL_SEQ_NBR` | DOUBLE | NOT NULL |  | The sequence number of this cell based on the pattern defined for the position map. |
| 5 | `CELL_TXT` | VARCHAR(40) | NOT NULL |  | The text to display in the cell. |
| 6 | `COL_NBR` | DOUBLE | NOT NULL |  | The column to which this cell belongs. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `MAP_NBR` | DOUBLE | NOT NULL |  | The map to which this cell belongs. |
| 9 | `PREV_UCM_POSITION_MAP_CELL_ID` | DOUBLE | NOT NULL |  | This field is used to track versions of the protocol batch item map cell information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective date/times. |
| 10 | `ROW_NBR` | DOUBLE | NOT NULL |  | The row to which this cell belongs. |
| 11 | `UCMR_POSITION_MAP_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the reference position map to which this cell is associated. |
| 12 | `UCM_POSITION_MAP_CELL_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a row for each cell in the position map for a protocol batch which stores the details about that cell. |
| 13 | `UCM_PTL_BATCH_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the batch item to which this position map cell is associated. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UCMR_POSITION_MAP_ID` | [UCMR_POSITION_MAP](UCMR_POSITION_MAP.md) | `UCMR_POSITION_MAP_ID` |
| `UCM_PTL_BATCH_ITEM_ID` | [UCM_PTL_BATCH_ITEM](UCM_PTL_BATCH_ITEM.md) | `UCM_PTL_BATCH_ITEM_ID` |

