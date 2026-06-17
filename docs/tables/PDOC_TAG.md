# PDOC_TAG

> This table captures data about items a user tags, i.e. marks as an item of interest.

**Description:** Physician Documentation Tag  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATEGORIZATION_XML` | VARCHAR(3000) |  |  | Defines categorization of tagged item on clipboard |
| 2 | `EMR_TYPE_CD` | DOUBLE | NOT NULL |  | Used to determine the format applied to the tagged item. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter record related to the tagged item. |
| 4 | `PDOC_TAG_ID` | DOUBLE | NOT NULL |  | Uniqiuely identifies a tagged item. |
| 5 | `REFERENCE_UUID` | VARCHAR(255) | NOT NULL |  | Identifier created to uniquely identify a tagged item prior to inserting a row into the TAG table. |
| 6 | `TAG_DT_TM` | DATETIME | NOT NULL |  | The date and time the tag was initially created. |
| 7 | `TAG_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifier used to query for the tagged item. |
| 8 | `TAG_ENTITY_NAME` | VARCHAR(255) | NOT NULL |  | Contains the name of the entity related to the tag. |
| 9 | `TAG_USER_ID` | DOUBLE | NOT NULL | FK→ | Contains the Id of the person that created the tags. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `TAG_USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

