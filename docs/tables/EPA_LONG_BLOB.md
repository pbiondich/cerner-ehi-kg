# EPA_LONG_BLOB

> Stores BLOB data for Electronic Authorization

**Description:** Electronic Prior Authorization Long Blob  
**Table type:** ACTIVITY  
**Primary key:** `EPA_LONG_BLOB_ID`  
**Columns:** 8  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `EPA_LONG_BLOB_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 3 | `LONG_BLOB` | LONGBLOB |  |  | The BLOB data to be stored on the EPA_LONG_BLOB table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [EPA_ACTIVITY](EPA_ACTIVITY.md) | `EPA_QUESTION_SET_BLOB_ID` |
| [EPA_RECORD](EPA_RECORD.md) | `EPA_MEDICATION_BLOB_ID` |
| [EPA_RECORD](EPA_RECORD.md) | `EPA_PATIENT_DEMOG_BLOB_ID` |

