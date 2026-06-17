# WORKING_VIEW_PERSON_SECT

> Specifies the definition for working views that are applicable for a given encounter.

**Description:** Specifies the definition for working views that are applicable for a given encnt  
**Table type:** ACTIVITY  
**Primary key:** `WORKING_VIEW_PERSON_SECT_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_SET_NAME` | VARCHAR(40) | NOT NULL |  | Specifies the child event sets associated to a working view. |
| 2 | `INCLUDED_IND` | DOUBLE | NOT NULL |  | Specifies whether the event set is included on the working view. |
| 3 | `SECTION_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of the section (0=event set; 1=IV Drip) |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `WORKING_VIEW_PERSON_ID` | DOUBLE | NOT NULL | FK→ | FK from the working_view_person table. |
| 10 | `WORKING_VIEW_PERSON_SECT_ID` | DOUBLE | NOT NULL | PK | Primary Key |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `WORKING_VIEW_PERSON_ID` | [WORKING_VIEW_PERSON](WORKING_VIEW_PERSON.md) | `WORKING_VIEW_PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [WORKING_VIEW_PERSONITEM](WORKING_VIEW_PERSONITEM.md) | `WORKING_VIEW_PERSON_SECT_ID` |

