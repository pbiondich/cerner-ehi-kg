# LH_ABS_MEASURE_RELTN

> Contains measure info for each condition

**Description:** LH_ABS_MEASURE_RELTN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the category which the quality measures are associated with. Foreign key to the BR_DATAMART_CATEGORY table. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 6 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 7 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 9 | `LH_ABS_LAYOUT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the layout row which the measure is associated with. Foreign key to the LH_ABS_LAYOUT table. |
| 10 | `LH_ABS_MEASURE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the measure which the condition is associated with. Foreign key to the LH_ABS_MEASURE table. |
| 11 | `LH_ABS_MEASURE_RELTN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_MEASURE_RELTN table. |
| 12 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time that the record was partitioned |
| 13 | `PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was processed |
| 14 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 17 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_DATAMART_CATEGORY_ID` | [BR_DATAMART_CATEGORY](BR_DATAMART_CATEGORY.md) | `BR_DATAMART_CATEGORY_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_ABS_LAYOUT](LH_ABS_LAYOUT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_ABS_MEASURE](LH_ABS_MEASURE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `LH_ABS_LAYOUT_ID` | [LH_ABS_LAYOUT](LH_ABS_LAYOUT.md) | `LH_ABS_LAYOUT_ID` |
| `LH_ABS_MEASURE_ID` | [LH_ABS_MEASURE](LH_ABS_MEASURE.md) | `LH_ABS_MEASURE_ID` |

