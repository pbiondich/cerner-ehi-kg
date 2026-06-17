# SPECIMEN_GROUPING_R

> This reference table contains specimen groupings that can optionally be associated with a case prefix. Specimen groupings (sublists of specimens from codeset 1306) provide an option for the specimen list to be more specific to the case prefix.

**Description:** Specimen Grouping Reltn  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATEGORY_CD` | DOUBLE | NOT NULL | FK→ | This field stores the foreign key reference to the specimen groupings (stored on codeset 1312). |
| 2 | `SOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field stores the foreign key reference to the specimens (stored on codeset 1306) associated to the specimen groupings (stored on codeset 1312). |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATEGORY_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SOURCE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

