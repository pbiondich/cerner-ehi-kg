# WORKING_VIEW_PERSON

> Specifies the working views that are applicable for a given patient encounter.

**Description:** WORKING VIEW PERSON  
**Table type:** ACTIVITY  
**Primary key:** `WORKING_VIEW_PERSON_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 2 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 8 | `WORKING_VIEW_ID` | DOUBLE | NOT NULL | FK→ | The working view id that links this person centric content to the view content defined for a given position/location. |
| 9 | `WORKING_VIEW_PERSON_ID` | DOUBLE | NOT NULL | PK | Primary Key. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `WORKING_VIEW_ID` | [WORKING_VIEW](WORKING_VIEW.md) | `WORKING_VIEW_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [WORKING_VIEW_PERSON_SECT](WORKING_VIEW_PERSON_SECT.md) | `WORKING_VIEW_PERSON_ID` |

