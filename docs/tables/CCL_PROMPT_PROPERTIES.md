# CCL_PROMPT_PROPERTIES

> This table defines a prompt control's specific properties on a CCL form.

**Description:** CCL Prompt Properties  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPONENT_NAME` | VARCHAR(30) | NOT NULL |  | Control sub component name storing this property. |
| 2 | `PROMPT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key references CCL_PROMPT_DEFINITIONS(PROMPT_ID). |
| 3 | `PROPERTY_NAME` | VARCHAR(30) | NOT NULL |  | Control sub-component property name. Must be unique to the component. |
| 4 | `PROPERTY_VALUE` | VARCHAR(1000) |  |  | Textual representation of the properties value(s). |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROMPT_ID` | [CCL_PROMPT_DEFINITIONS](CCL_PROMPT_DEFINITIONS.md) | `PROMPT_ID` |

