# ASSEMBLY_PART

> Provides the list of parts for an assembly created by a lab system.

**Description:** Assembly Part  
**Table type:** ACTIVITY  
**Primary key:** `ASSEMBLY_PART_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASSEMBLY_IDENT` | VARCHAR(40) |  |  | The unique identifier of the assembly this part is for from the source system. |
| 3 | `ASSEMBLY_PART_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a list of parts for an assembly created by a lab system. |
| 4 | `ASSEMBLY_PUBLICATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related assembly publication for the assembly this part is for. |
| 5 | `COMPONENT_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of component for this assembly part on the assembly. |
| 6 | `EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date from which the assembly part is effective. |
| 7 | `LOCATOR_LAB_SYSTEM_NAME` | VARCHAR(40) | NOT NULL |  | The lab system that created the assembly part for the assembly. |
| 8 | `LOCATOR_NAME` | VARCHAR(40) | NOT NULL |  | The locator name in the lab system that created the assembly part for the assembly. |
| 9 | `LOCATOR_TAG_TXT` | VARCHAR(40) | NOT NULL |  | The tag for the locator in the lab system that created the assembly part for the assembly. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSEMBLY_PUBLICATION_ID` | [ASSEMBLY_PUBLICATION](ASSEMBLY_PUBLICATION.md) | `ASSEMBLY_PUBLICATION_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [ASSEMBLY_PART_LOCATOR](ASSEMBLY_PART_LOCATOR.md) | `ASSEMBLY_PART_ID` |
| [ASSEMBLY_TWEET_LOCATOR](ASSEMBLY_TWEET_LOCATOR.md) | `ASSEMBLY_PART_ID` |

