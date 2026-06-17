# ASSEMBLY_PART_LOCATOR

> Provides record locators for assembly parts.

**Description:** Assembly Part Locator  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASSEMBLY_PART_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the assembly part the locator is for |
| 3 | `ASSEMBLY_PART_LOCATOR_ID` | DOUBLE | NOT NULL |  | Uniquely identifies record locators for assembly parts. |
| 4 | `EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date from which the locator is effective. |
| 5 | `LAB_SYSTEM_ENTITY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the record in the lab system that is referenced by the locator for the assembly. |
| 6 | `LAB_SYSTEM_ENTITY_NAME` | VARCHAR(40) | NOT NULL |  | The name of the record identifier in the lab system that is referenced by the locator for the assembly. |
| 7 | `LAB_SYSTEM_NAME` | VARCHAR(40) | NOT NULL |  | The lab system that created the locator for the assembly. |
| 8 | `LOCATOR_NAME` | VARCHAR(40) | NOT NULL |  | The name of the locator in the lab system that created the locator for the assembly. |
| 9 | `LOCATOR_TAG_TXT` | VARCHAR(40) | NOT NULL |  | The tag for the locator in the lab system that created the locator for the assembly. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSEMBLY_PART_ID` | [ASSEMBLY_PART](ASSEMBLY_PART.md) | `ASSEMBLY_PART_ID` |

