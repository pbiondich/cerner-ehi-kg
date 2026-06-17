# PDOC_TAG_TEXT

> This table captures data about Text items that a user tags, i.e. marks as an item of interest.

**Description:** Physicain Doc Tag Text  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Contains the encounter ID associated with the tagged item. |
| 2 | `FORMAT_CD` | DOUBLE | NOT NULL |  | The format of the text, e.g. RTF, HTML or ASCII |
| 3 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies where the text is stored. |
| 4 | `PDOC_TAG_TEXT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies text related to a tag. |
| 5 | `REFERENCE_UUID` | VARCHAR(255) | NOT NULL |  | Created to identify tagged item prior to inserting a row into the TAG_TEXT table. |
| 6 | `TAG_DT_TM` | DATETIME | NOT NULL |  | Date and Time the item was tagged. |
| 7 | `TAG_ENTITY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the entity related to this tag. |
| 8 | `TAG_ENTITY_NAME` | VARCHAR(255) | NOT NULL |  | Contains the name of the entity related to the tag. |
| 9 | `TAG_USER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the user that created the tag. |
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
| `LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `TAG_USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

