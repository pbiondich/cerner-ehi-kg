# PREGNANCY_CHILD_ENTITY_R

> Maintains relationships to various entities related to a child of a pregnancy (for example: code set values, clinical events, and nomenclatures)

**Description:** Pregnancy Child Entity Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `COMPONENT_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of related data that the entity represents for the child |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifies the related entity on its parent table |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | NAME OF PARENT TABLE FOR PARENT ENTITY ID |
| 7 | `PREGNANCY_CHILD_ENTITY_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 8 | `PREGNANCY_CHILD_ID` | DOUBLE | NOT NULL | FK→ | Identifies the child on PREGNANCY_CHILD that the entity is related to |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREGNANCY_CHILD_ID` | [PREGNANCY_CHILD](PREGNANCY_CHILD.md) | `PREGNANCY_CHILD_ID` |

