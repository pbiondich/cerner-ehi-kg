# PW_COMP_ACT_RELTN

> This table holds the relationship between component and the phase

**Description:** Pathway component phase activity relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACT_PW_COMP_ID` | DOUBLE | NOT NULL | FK→ | Pathway component identification. Unique id of the pathway comp entry referenced by an entry on this table. |
| 2 | `PATHWAY_ID` | DOUBLE | NOT NULL | FK→ | Pathway catalog identification. Unique id of the pathway catalog entry referenced by an entry on this table. |
| 3 | `PW_COMP_ACT_RELTN_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `TYPE_MEAN` | VARCHAR(12) | NOT NULL |  | Indicates the type of relationship between the component and pathway catalog. Possible values - SCHEDANCHOR. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACT_PW_COMP_ID` | [ACT_PW_COMP](ACT_PW_COMP.md) | `ACT_PW_COMP_ID` |
| `PATHWAY_ID` | [PATHWAY](PATHWAY.md) | `PATHWAY_ID` |

