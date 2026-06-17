# BH_GROUP_DOC_PATIENT

> The patient that participates in the group therapy session.

**Description:** Behavioral Health Group Documentation Patient  
**Table type:** ACTIVITY  
**Primary key:** `BH_GROUP_DOC_PATIENT_ID`  
**Columns:** 19  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ATTEND_CD` | DOUBLE | NOT NULL |  | Identifier if the patient attended the therapy session. |
| 6 | `BEGIN_DT_TM` | DATETIME | NOT NULL |  | The date and time the patient arrived for the session. |
| 7 | `BH_GROUP_DOC_ID` | DOUBLE | NOT NULL | FK→ | The session that this patient was scheduled to attend. |
| 8 | `BH_GROUP_DOC_PATIENT_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the BH_GROUP_DOC_PATIENT table. |
| 9 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter for this patient in this session. |
| 10 | `END_DT_TM` | DATETIME | NOT NULL |  | The date and time the patient left the therapy session. |
| 11 | `EVENT_ID` | DOUBLE | NOT NULL |  | The clinical note created for the patient. |
| 12 | `HIGH_PRIORITY_IND` | DOUBLE | NOT NULL |  | To flag specific clinical notes as important for easier referenceability and review at a later date. |
| 13 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The patient that is scheduled for this therapy session. |
| 14 | `SESSION_LENGTH_MINS` | DOUBLE | NOT NULL |  | The number of minutes this patient attended the session. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BH_GROUP_DOC_ID` | [BH_GROUP_DOC](BH_GROUP_DOC.md) | `BH_GROUP_DOC_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [BH_GROUP_DOC_PATIENT_ATTR](BH_GROUP_DOC_PATIENT_ATTR.md) | `BH_GROUP_DOC_PATIENT_ID` |
| [BH_GROUP_DOC_PATIENT_CS](BH_GROUP_DOC_PATIENT_CS.md) | `BH_GROUP_DOC_PATIENT_ID` |

