# CP_PATHWAY

> Contain definition and configuration of nodes used in Care Planning Pathways.

**Description:** Care Planning Pathway  
**Table type:** REFERENCE  
**Primary key:** `CP_PATHWAY_ID`  
**Columns:** 17  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CP_CONCEPT_CD` | DOUBLE | NOT NULL |  | Identifies what concept code the pathway is related to. |
| 6 | `CP_PATHWAY_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 7 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 8 | `OWNER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Indicates the owner of the pathway if this is a customized pathway (User level bundle). For General bundles, the value will be zero. |
| 9 | `PATHWAY_DIAGRAM_URL` | VARCHAR(1000) |  |  | The URL that points to the overall diagram for this pathway. |
| 10 | `PATHWAY_NAME` | VARCHAR(100) | NOT NULL |  | The name of the pathway being stored. |
| 11 | `PATHWAY_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the pathway being stored. |
| 12 | `PATHWAY_TYPE_CD` | DOUBLE | NOT NULL |  | The type of pathway being stored. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `OWNER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [CP_NODE](CP_NODE.md) | `CP_PATHWAY_ID` |
| [CP_PATHWAY_ACTIVITY](CP_PATHWAY_ACTIVITY.md) | `CP_PATHWAY_ID` |
| [CP_PATHWAY_GROUP_R](CP_PATHWAY_GROUP_R.md) | `CP_PATHWAY_ID` |
| [CP_TRIGGERING_CRITERIA](CP_TRIGGERING_CRITERIA.md) | `CP_PATHWAY_ID` |

