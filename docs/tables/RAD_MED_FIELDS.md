# RAD_MED_FIELDS

> This table contains the definition of fields that will be captured as a part of recording medications administered within the Radiology department.

**Description:** Rad Med Fields  
**Table type:** REFERENCE  
**Primary key:** `RAD_MED_FIELD_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `FIELD_DESCRIPTION` | VARCHAR(60) |  |  | This column contains the description of the field. |
| 6 | `FIELD_MEANING` | VARCHAR(12) |  |  | This column contains the meaning of the field that can used by the application to identify the purpose of the field. |
| 7 | `FIELD_TYPE_FLAG` | DOUBLE |  |  | This column indicates what type of data type is to be captured for a given field. (1 - numeric, 2 - string, 3 - date) |
| 8 | `RAD_MED_FIELD_ID` | DOUBLE | NOT NULL | PK | This column contains a meaningless number used only to serve as a unique identifier for the row. |
| 9 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | This column holds an indicator which is used to determine if the medication field is required or not |
| 10 | `SEQUENCE` | DOUBLE |  |  | This column indicates the order in which the fields should appear. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RAD_MED_DETAILS](RAD_MED_DETAILS.md) | `RAD_MED_FIELD_ID` |

