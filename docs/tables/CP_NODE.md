# CP_NODE

> Contain definition and links for configuration of a Node in Care Planning workflow

**Description:** Care Planning Node  
**Table type:** REFERENCE  
**Primary key:** `CP_NODE_ID`  
**Columns:** 21  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CATEGORY_MEAN` | VARCHAR(30) |  |  | The Category Meaning. This column maps to the CATEGORY_MEAN column in Bedrock trable BR_DATAMART_CATEGORY if Bedrock is in the domain. Otherwise the value is nulls. |
| 4 | `COLLATION_SEQ` | DOUBLE |  |  | Provides the ability to sequence the list of nodes within a pathway for display purposes |
| 5 | `CONCEPT_CD` | DOUBLE | NOT NULL |  | Concept code used to uniquely identify the concept |
| 6 | `CP_NODE_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 7 | `CP_PATHWAY_ID` | DOUBLE | NOT NULL | FK→ | FK Value form CP_PATHWAY table |
| 8 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Date and time when the NODE record was created |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `INTENTION_CD` | DOUBLE | NOT NULL |  | INTENTION CODE |
| 11 | `NODE_DISPLAY` | VARCHAR(255) |  |  | The data that will be displayed on the user interface |
| 12 | `NODE_NAME` | VARCHAR(100) | NOT NULL |  | Name of node for display/linking purposes in build tool |
| 13 | `PUBLISH_IND` | DOUBLE | NOT NULL |  | Used for indicate that the content is ready for display on the user interface. |
| 14 | `TREATMENT_LINE_CD` | DOUBLE | NOT NULL |  | The Treatment Line represented by this node |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 20 | `VERSION_NODE_ID` | DOUBLE | NOT NULL | FK→ | The originating NODE_ID for this version. Used to support Type-2 Versioning in the table. |
| 21 | `VERSION_TEXT` | VARCHAR(4000) |  |  | Information about a version of the NODE |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CP_PATHWAY_ID` | [CP_PATHWAY](CP_PATHWAY.md) | `CP_PATHWAY_ID` |
| `VERSION_NODE_ID` | [CP_NODE](CP_NODE.md) | `CP_NODE_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [CP_COMPONENT](CP_COMPONENT.md) | `CP_NODE_ID` |
| [CP_NODE](CP_NODE.md) | `VERSION_NODE_ID` |
| [CP_NODE_BEHAVIOR](CP_NODE_BEHAVIOR.md) | `CP_NODE_ID` |
| [CP_PATHWAY_ACTION](CP_PATHWAY_ACTION.md) | `CP_NODE_ID` |

