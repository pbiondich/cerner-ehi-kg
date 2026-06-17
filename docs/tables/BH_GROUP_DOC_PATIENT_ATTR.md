# BH_GROUP_DOC_PATIENT_ATTR

> Information that pertains to the patient schedule for the therapy session.

**Description:** Behavioral Health Group Documentation Patient Attribute  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BH_GROUP_DOC_PATIENT_ATTR_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the BH_GROUP_DOC_PATIENT_ATTR table. |
| 2 | `BH_GROUP_DOC_PATIENT_ID` | DOUBLE | NOT NULL | FK→ | The patient that the information on this row pertains to. |
| 3 | `COLLATION_SEQ` | DOUBLE | NOT NULL |  | Used to define ordering of section. Example : If more than one goal is defined for a patient, Goal1, Goal2, Goal3, etc. collation_seq used to decide the order. |
| 4 | `MPAGE_SECTION_NAME` | VARCHAR(255) | NOT NULL |  | The name of the mPage section. |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The Unique Identifier from the corresponding table referenced in PARENT_ENTITY_NAME which identifies patient attribute. Example : If a goal defined for a patient, Patient's achievement for the goal will be a code value. In this case PARENT_ENTITY_NAME will be CODE_VALUE and parent_entity_id will be its identifier. |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The name of the table used to find the information recorded in parent_entity_name. |
| 7 | `SECTION_TITLE_TXT` | VARCHAR(255) | NOT NULL |  | Used for dynamic titles of certain attributes. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BH_GROUP_DOC_PATIENT_ID` | [BH_GROUP_DOC_PATIENT](BH_GROUP_DOC_PATIENT.md) | `BH_GROUP_DOC_PATIENT_ID` |

