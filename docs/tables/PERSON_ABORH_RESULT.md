# PERSON_ABORH_RESULT

> The result of every ABO/Rh procedure performed and verified on a person, with an association to thehistorical ABO/Rh active on the person at the time of the result.

**Description:** Person Aborh Result  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CONTAINER_ID` | DOUBLE | NOT NULL | FK→ | Indicates the container for the specimen. Unique identifier from the Container table |
| 6 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 7 | `DONOR_ABORH_ID` | DOUBLE | NOT NULL |  | Created from same result as PERSON_ABORH_RESULT identifying record from the DONOR_ABORH which defines the current historical ABO/Rh of a donor. Used by donor applications to validate the product's ABO/Rh against the donor's ABO/Rh. |
| 8 | `DRAWN_DT_TM` | DATETIME |  |  | Indicates the date and time that the specimen was drawn/collected, populated from the COLLECTION table. |
| 9 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 10 | `PERSON_ABORH_ID` | DOUBLE | NOT NULL | FK→ | Link to PERSON_ABORH row created from same result as PERSON_ABORH_RESULT row. Unique identifier from the PERSON_ABORH table. |
| 11 | `PERSON_ABORH_RS_ID` | DOUBLE | NOT NULL |  | The primary key of this table. An internal system-assigned number that makes each row unique. |
| 12 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 13 | `RESULT_CD` | DOUBLE | NOT NULL |  | The ABORh result verified for the person (ex. "O Pos", "A Neg", etc.). |
| 14 | `RESULT_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the RESULT table. It is an internal system-assigned number. On this table, it identifies the ABORh result verified for the person. |
| 15 | `SPECIMEN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the specimen. Unique identifier from V500_SPECIMEN table |
| 16 | `STANDARD_ABORH_CD` | DOUBLE | NOT NULL |  | Stores the standard ABO/RH associated with the ABO/RH result verified for the person. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTAINER_ID` | [CONTAINER](CONTAINER.md) | `CONTAINER_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ABORH_ID` | [PERSON_ABORH](PERSON_ABORH.md) | `PERSON_ABORH_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RESULT_ID` | [RESULT](RESULT.md) | `RESULT_ID` |
| `SPECIMEN_ID` | [V500_SPECIMEN](V500_SPECIMEN.md) | `SPECIMEN_ID` |

