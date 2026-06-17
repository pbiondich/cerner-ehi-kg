# CP_NODE_BEHAVIOR

> Contains behaviors between pathway nodes and the possible reactions from decisions available in the nodes.

**Description:** CARE PLANNING NODE BEHAVIOR  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CP_NODE_BEHAVIOR_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 2 | `CP_NODE_ID` | DOUBLE | NOT NULL | FK→ | the node that is currently in context.for a certain node within a pathway what are the responses based on the RESPONSE_IDENT. |
| 3 | `INSTANCE_IDENT` | VARCHAR(255) |  |  | Identifier used to reference correct version of DD_SREF_TEMPLATE.DD_SREF_TMPL_INSTANCE_IDENT |
| 4 | `LONG_RESPONSE_IDENT` | LONGTEXT |  |  | LONG verbose form of the identifier that is generated from a correlating dynamic document being used in the pathway/node. |
| 5 | `REACTION_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a reaction type for the REACTION_ENTITY_NAME. |
| 6 | `REACTION_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The name of the reaction that is to occur in the pathway/node process (ORDER_CATALOG, NOMENCLATURE, CODE_VALUE, CP_NODE,ORDER_CATALOG_SYNONYM, ORDER_SENTENCE). |
| 7 | `REACTION_TYPE_MEAN` | VARCHAR(100) | NOT NULL |  | A type categorization of the Reaction |
| 8 | `RESPONSE_IDENT` | VARCHAR(1000) | NOT NULL |  | A unique string identifier that is generated from a correlating dynamic document being used in the pathway/node. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CP_NODE_ID` | [CP_NODE](CP_NODE.md) | `CP_NODE_ID` |

