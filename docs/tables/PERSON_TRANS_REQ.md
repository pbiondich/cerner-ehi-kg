# PERSON_TRANS_REQ

> Contains the transfusion requirements for a person, as entered by the blood bank, e.g., irradiated blood needed, CMV negative blood needed, etc.

**Description:** Person Transfusion Requirements  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADDED_DT_TM` | DATETIME |  |  | Indicates the date and time that a transfusion requireent is added for the specified person. |
| 6 | `ADDED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the personnel who added the transfusion requirement for the specidied person. |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 10 | `PERSON_TRANS_REQ_ID` | DOUBLE | NOT NULL |  | This is the primary key of this table. It is an internal system-assigned number that makes each row unique. |
| 11 | `REMOVED_DT_TM` | DATETIME |  |  | Indicates the date and time that a transfusion requirement is removed for the specified person. |
| 12 | `REMOVED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the personnel who removed the transfusion for the specified person. |
| 13 | `REQUIREMENT_CD` | DOUBLE | NOT NULL |  | Defines a requirement or restriction of transfusing this person with blood products. Something other than normal protocol that is required when dispensing any blood products to this patient, in order to keep from adversely affecting their health. Examples are: irradiation (all blood must be irradiated before being infused), CMV Negative (alll blood must be tested for being CMV negative before being infused), etc. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ADDED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REMOVED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

