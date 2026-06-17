# SN_SIGNATURE

> Stores the history of electronic signature of SurgiNet documents, segments, and field results.

**Description:** SurgiNet Electronic Signature History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | The date and time of a signature or an override of a required signature. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `COMMENT_TXT` | VARCHAR(255) |  |  | Stores the comment of a signature, or a reason for overriding a required signature. |
| 7 | `OVERRIDE_IND` | DOUBLE | NOT NULL |  | 0 indicates that this is a signature. 1 indicates that this is an override of a required signature. |
| 8 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The primary key ID of the table in PARENT_ENTITY_NAME that identifies the signed entity. |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | Identifies the signed entity, i.e.: PERIOPERATIVE_DOCUMENT, INPUT_FORM_DEFINITION, etc. |
| 10 | `PERIOP_DOC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the document. Foreign Key from PERIOPERATIVE_DOCUMENT |
| 11 | `PERSONNEL_ID` | DOUBLE | NOT NULL | FK→ | The person_id of the personnel that signed a document, a segment, or a field result, or overrode a required signature. |
| 12 | `SIGNATURE_ID` | DOUBLE | NOT NULL |  | The primary key ID that uniquely identifies an electronic signature, or an override of a required signature. |
| 13 | `TEMPORARY_IND` | DOUBLE | NOT NULL |  | 0 indicates that this is not a temporary signature. 1 indicates that this is a temporary signature that has not been stored in the clinical repository. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERIOP_DOC_ID` | [PERIOPERATIVE_DOCUMENT](PERIOPERATIVE_DOCUMENT.md) | `PERIOP_DOC_ID` |
| `PERSONNEL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

