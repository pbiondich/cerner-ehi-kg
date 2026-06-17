# CP_COMPONENT

> Contain definition and links for configuration of a care planning component

**Description:** Care Planning Component  
**Table type:** REFERENCE  
**Primary key:** `CP_COMPONENT_ID`  
**Columns:** 11  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPONENT_DISPLAY` | VARCHAR(255) | NOT NULL |  | Optional display value for the component. |
| 2 | `COMPONENT_SEQ_TXT` | VARCHAR(10) |  |  | This will be a textual representation of how the component Is layed out on the screen in the format of "GROUP:ROW:COL" |
| 3 | `COMP_TYPE_CD` | DOUBLE | NOT NULL |  | Type of care planning component |
| 4 | `CONCEPT_GROUP_CD` | DOUBLE | NOT NULL |  | The concept group that this component loads configuration data from. |
| 5 | `CP_COMPONENT_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 6 | `CP_NODE_ID` | DOUBLE | NOT NULL | FK→ | Node that this component is linked to |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CP_NODE_ID` | [CP_NODE](CP_NODE.md) | `CP_NODE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CP_COMPONENT_DETAIL](CP_COMPONENT_DETAIL.md) | `CP_COMPONENT_ID` |
| [CP_PATHWAY_ACTION](CP_PATHWAY_ACTION.md) | `CP_COMPONENT_ID` |

