# UCM_PTL_RESULT

> Stores protocol results for a protocol batch item.

**Description:** Unified Case Manager - Protocol Result  
**Table type:** ACTIVITY  
**Primary key:** `UCM_PTL_RESULT_ID`  
**Columns:** 22  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCEPT_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of accept for this result. Stored here in case the result is converted to a different accept type, and the new type is tracked here. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `FROM_PTL_RESULT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the ucm_ptl_result_id from which this result's snapshot was taken. |
| 7 | `PREV_UCM_PTL_RESULT_ID` | DOUBLE | NOT NULL |  | This field is used to track versions of the protocol result information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 8 | `RESULT_CD` | DOUBLE | NOT NULL |  | Stores result for accept type of coded list (item selected from list). Note, this can be code value from any code set, since the available values for a code list are the values from any code set chosen for the worksheet statement. |
| 9 | `RESULT_DT_TM` | DATETIME |  |  | Stores result for the accept type of date and time, and date. |
| 10 | `RESULT_FLAG` | DOUBLE | NOT NULL |  | Stores extra information pertaining to results. This field is a bitwise combination of flag values to allow multiple values to be stored at the same time. |
| 11 | `RESULT_NBR` | DOUBLE | NOT NULL |  | Stores result for accept types of Checkbox (1 = Checked), Numeric, Calculation, and Time. For time, a 4 digit number will be saved. Note a time result will not be adjusted for UTC since it is stored this way. |
| 12 | `RESULT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Stores results for the accept type of Personnel ID |
| 13 | `RESULT_TXT` | VARCHAR(250) | NOT NULL |  | Stores result for accept type of Text and will store the appropriate textual representation of all other accept types as well. |
| 14 | `RESULT_TZ` | DOUBLE | NOT NULL |  | Time zone associated with the corresponding RESULT_DT_TM column. |
| 15 | `UCMR_WORKSHEET_STATEMENT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the reference side worksheet statement this result represents. |
| 16 | `UCM_PTL_BATCH_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the batch item (order/container) to which this result applies. |
| 17 | `UCM_PTL_RESULT_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a given protocol result. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FROM_PTL_RESULT_ID` | [UCM_PTL_RESULT](UCM_PTL_RESULT.md) | `UCM_PTL_RESULT_ID` |
| `RESULT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `UCMR_WORKSHEET_STATEMENT_ID` | [UCMR_WORKSHEET_STATEMENT_R](UCMR_WORKSHEET_STATEMENT_R.md) | `UCMR_WORKSHEET_STATEMENT_R_ID` |
| `UCM_PTL_BATCH_ITEM_ID` | [UCM_PTL_BATCH_ITEM](UCM_PTL_BATCH_ITEM.md) | `UCM_PTL_BATCH_ITEM_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [UCM_PTL_RESULT](UCM_PTL_RESULT.md) | `FROM_PTL_RESULT_ID` |
| [UCM_REPORT_FIELD](UCM_REPORT_FIELD.md) | `UCM_PTL_RESULT_ID` |

