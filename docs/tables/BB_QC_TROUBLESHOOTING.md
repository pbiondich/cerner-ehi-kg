# BB_QC_TROUBLESHOOTING

> This table contains the possible troubleshooting steps that users can select from when a quality control result is determined to be out of control.

**Description:** Blood Bank Quality Control Troubleshooting Steps  
**Table type:** REFERENCE  
**Primary key:** `TROUBLESHOOTING_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `TROUBLESHOOTING_ID` | DOUBLE | NOT NULL | PK | This field contains the unique value that identifies troubleshooting step. |
| 5 | `TROUBLESHOOTING_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key identifier to the LONG_TEXT_REFERENCE table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TROUBLESHOOTING_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BB_QC_RESULT_TROUBLESHOOTING_R](BB_QC_RESULT_TROUBLESHOOTING_R.md) | `TROUBLESHOOTING_ID` |

