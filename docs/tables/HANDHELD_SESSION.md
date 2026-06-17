# HANDHELD_SESSION

> This table will be used to track information for each session from a handheld collection device. This table is used for reporting purposes only.

**Description:** Handheld Session  
**Table type:** ACTIVITY  
**Primary key:** `HANDHELD_SESSION_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEVICE_TXT` | VARCHAR(100) |  |  | The name of the device used for the handheld collections. |
| 2 | `HANDHELD_SESSION_ID` | DOUBLE | NOT NULL | PK | A unique identifier for each occurrence of a Handheld session. |
| 3 | `LOGON_DT_TM` | DATETIME | NOT NULL |  | The date and time the user logged onto the device. |
| 4 | `POSITIVE_PATIENT_IDENT_FLAG` | DOUBLE | NOT NULL |  | The preference value that indicates the level at which positive patient identification will be used. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [HANDHELD_UPLOAD](HANDHELD_UPLOAD.md) | `HANDHELD_SESSION_ID` |

