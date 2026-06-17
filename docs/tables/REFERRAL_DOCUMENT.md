# REFERRAL_DOCUMENT

> This table links documents to a referral. This includes clinical documents and CAMM documents.

**Description:** Referral Document  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BLOB_HANDLE` | VARCHAR(255) |  |  | The handle to the remote blob (CPDI) being referenced. |
| 6 | `CATEGORY_CD` | DOUBLE |  |  | This column defines the category of a document attached to a referral. |
| 7 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time that a row is created in the referral document table. |
| 8 | `DISPLAY_NAME` | VARCHAR(255) |  |  | A descriptive name for the document that can be displayed to the user. |
| 9 | `EVENT_ID` | DOUBLE | NOT NULL |  | The event identifier of the clinical document being referenced. |
| 10 | `MEDIA_OBJECT_IDENTIFIER` | VARCHAR(64) |  |  | The identifier of the external media object (CAMM) being referenced. |
| 11 | `MEDIA_OBJECT_VERSION_NBR` | DOUBLE | NOT NULL |  | The version number of the external media object (CAMM) being referenced. |
| 12 | `REFERRAL_DOCUMENT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the referral_document table. |
| 13 | `REFERRAL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the referral linked to the document. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | `REFERRAL_ID` |

