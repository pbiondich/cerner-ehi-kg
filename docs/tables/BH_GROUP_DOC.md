# BH_GROUP_DOC

> Information about a particular Behavioral Health Group session.

**Description:** Behavioral Health Group Documentation  
**Table type:** ACTIVITY  
**Primary key:** `BH_GROUP_DOC_ID`  
**Columns:** 32  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEGIN_DT_TM` | DATETIME | NOT NULL |  | Therapy session begin date and time |
| 2 | `BH_GROUP_DOC_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the BH_GROUP_DOC table. |
| 3 | `BILL_ITEM_CATALOG_CD` | DOUBLE | NOT NULL |  | Refers to a selected charge (bill_item) in Therapy Notes. |
| 4 | `CREATED_BY_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key value to PRSNL table - the person who created the note. |
| 5 | `CREATED_DT_TM` | DATETIME | NOT NULL |  | Create date and time of the Therapeutic Note |
| 6 | `DOC_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the documentation. |
| 7 | `END_DT_TM` | DATETIME | NOT NULL |  | Therapy session end date and time. |
| 8 | `GOALS_LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Goals set for the group. |
| 9 | `GROUP_SLOT_LINK_VALUE` | DOUBLE | NOT NULL |  | An identifier to link all the slots or/and appointments in the same group session together. |
| 10 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The Location where the session was held. |
| 11 | `NOTES_LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Narrative documentation for the group. |
| 12 | `NOTES_REFUSE_COMMENT_TXT` | VARCHAR(1000) |  |  | The reason a physician refused to accept the therapy session notes. |
| 13 | `NOTES_REFUSE_IND` | DOUBLE | NOT NULL |  | Indicates whether the physician refused to accept the notes submitted by a student. |
| 14 | `ORIG_BH_GROUP_DOC_ID` | DOUBLE | NOT NULL | FK→ | Used for building a hierarchy within the documents.Indvidual patient deails like behavior, notes, goalsetc. are available to capture initially, whereas a few patients details would be pending. So the note would be signed in batches and these batches will be related through this column. |
| 15 | `PATIENT_LIST_ID` | DOUBLE | NOT NULL | FK→ | Foreign key from DCP_PATIENT_LIST. Identifies from which Patient List Group document the patients should be pulled. |
| 16 | `PRI_FCLTR_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Primary facilitator who conducts the therapy session |
| 17 | `PROPOSED_BILL_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The charte item that the physician chose for the therapy session. |
| 18 | `SCH_APPT_ID` | DOUBLE | NOT NULL | FK→ | Schedule identifier connected to the Therapeutic Note. |
| 19 | `SCH_APPT_TYPE_FLAG` | DOUBLE |  |  | Appointment Type connected to Therapeutic Notes through Revenue cycle and scheduling |
| 20 | `SERVICE_TOPIC_CD` | DOUBLE | NOT NULL |  | The topic for the therapy session. |
| 21 | `SERVICE_TYPE_CD` | DOUBLE | NOT NULL |  | The service type for the therapy session. |
| 22 | `SESSION_LENGTH_MINS` | DOUBLE | NOT NULL |  | The length of the session in minutes. |
| 23 | `SESSION_MODE_CD` | DOUBLE | NOT NULL |  | Therapy session mode of facilitation. |
| 24 | `SESSION_MODIFIER_CD` | DOUBLE | NOT NULL |  | Refersto a Charge modifier (bill_item) connected to the Therapeutic Note. Session Modifier is an additional item for dropping charge, another bill_item for the session. This additional charge may or may not be selected by the user. |
| 25 | `SESSION_NAME` | VARCHAR(255) | NOT NULL |  | The title of the session. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `VERIFIED_BY_ID` | DOUBLE | NOT NULL | FK→ | Personnel ID that verified a Therapeutic Note. |
| 32 | `VOLUNTEER_INVOLVED_CD` | DOUBLE | NOT NULL |  | Indicates if any volunteer was involved in the therapy session. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATED_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `GOALS_LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `NOTES_LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `ORIG_BH_GROUP_DOC_ID` | [BH_GROUP_DOC](BH_GROUP_DOC.md) | `BH_GROUP_DOC_ID` |
| `PATIENT_LIST_ID` | [DCP_PATIENT_LIST](DCP_PATIENT_LIST.md) | `PATIENT_LIST_ID` |
| `PRI_FCLTR_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PROPOSED_BILL_ITEM_ID` | [BILL_ITEM](BILL_ITEM.md) | `BILL_ITEM_ID` |
| `SCH_APPT_ID` | [SCH_APPT](SCH_APPT.md) | `SCH_APPT_ID` |
| `VERIFIED_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [BH_GROUP_DOC](BH_GROUP_DOC.md) | `ORIG_BH_GROUP_DOC_ID` |
| [BH_GROUP_DOC_PATIENT](BH_GROUP_DOC_PATIENT.md) | `BH_GROUP_DOC_ID` |
| [BH_GROUP_DOC_PRSNL](BH_GROUP_DOC_PRSNL.md) | `BH_GROUP_DOC_ID` |

