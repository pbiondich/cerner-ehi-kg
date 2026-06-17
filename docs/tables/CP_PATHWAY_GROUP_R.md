# CP_PATHWAY_GROUP_R

> Used to relate Pathways to Pathway Groups

**Description:** Care Planning Pathway Group Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CP_PATHWAY_GROUP_ID` | DOUBLE | NOT NULL | FK→ | This identifies the CP Pathway Group being associated to the CP Pathway. Foreign Key from the CP_PATHWAY_GROUP Table |
| 2 | `CP_PATHWAY_GROUP_R_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CP_PATHWAY_GROUP_R table. |
| 3 | `CP_PATHWAY_ID` | DOUBLE | NOT NULL | FK→ | This identifies a row fromthe CP Pathway tabel which is being related to a CP Pathway Group. Foreign Key from the CP_PATHWAY Table |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CP_PATHWAY_GROUP_ID` | [CP_PATHWAY_GROUP](CP_PATHWAY_GROUP.md) | `CP_PATHWAY_GROUP_ID` |
| `CP_PATHWAY_ID` | [CP_PATHWAY](CP_PATHWAY.md) | `CP_PATHWAY_ID` |

