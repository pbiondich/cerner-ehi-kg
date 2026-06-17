# HANDHELD_UPLOAD

> This table will be used to track information for each upload of data from a handheld collection device. This table is used for reporting purposes only.

**Description:** Handheld Upload  
**Table type:** ACTIVITY  
**Primary key:** `HANDHELD_UPLOAD_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEVICE_DT_TM` | DATETIME |  |  | If a significant date/time difference is detected on the upload, but the user chooses to continue with the upload, the date and time on the device will be stored here. If no discrepancy was found, this will be set to NULL. |
| 2 | `HANDHELD_SESSION_ID` | DOUBLE | NOT NULL | FK→ | A unique identifier for each occurrence of a Handheld session. |
| 3 | `HANDHELD_UPLOAD_ID` | DOUBLE | NOT NULL | PK | Unique identifier for each occurrence of an upload of data. |
| 4 | `LOGIN_LOCATION_CD` | DOUBLE | NOT NULL |  | Login location where the specimens where received. |
| 5 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization the user is performing the handheld collections for. |
| 6 | `REPORT_NBR` | DOUBLE | NOT NULL |  | A number assigned to each upload event that will be reset to 1 at the beginning of each day. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `UPLOAD_DT_TM` | DATETIME |  |  | The date and time the upload was performed. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HANDHELD_SESSION_ID` | [HANDHELD_SESSION](HANDHELD_SESSION.md) | `HANDHELD_SESSION_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [HANDHELD_DETAIL](HANDHELD_DETAIL.md) | `HANDHELD_UPLOAD_ID` |

