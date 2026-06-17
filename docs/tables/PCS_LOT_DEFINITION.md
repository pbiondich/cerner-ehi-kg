# PCS_LOT_DEFINITION

> This table stores the static definition information for a PathNet lot.

**Description:** PathNet Common Services Lot Definition  
**Table type:** ACTIVITY  
**Primary key:** `LOT_DEFINITION_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | This field allows the lot definitions to be grouped and filtered by the type of activity the lot will be used for (i.e. Microbiology, Blood Bank, etc. |
| 2 | `AVAILABLE_IND` | DOUBLE | NOT NULL |  | This field indicates when a lot definition is ready to be put into use for patient results. |
| 3 | `COMMENT_TEXT_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the LONG_TEXT row that contains the lot definition comment text. |
| 4 | `KIT_DEFINITION_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier of the associated kit definition. |
| 5 | `LOT_DEFINITION_ID` | DOUBLE | NOT NULL | PK | This field contains the unique value that identifies a lot definition |
| 6 | `MANUFACTURER_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the manufacturer associated with the lot definition. |
| 7 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier for the component associated with the lot definition. |
| 8 | `PARENT_ENTITY_NAME` | CHAR(30) | NOT NULL |  | This field contains the name of the table that the parent_entity_id is associated with. |
| 9 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the service resource associated with the lot definition. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `KIT_DEFINITION_ID` | [PCS_KIT_DEFINITION](PCS_KIT_DEFINITION.md) | `KIT_DEFINITION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PCS_LOT_INFORMATION](PCS_LOT_INFORMATION.md) | `LOT_DEFINITION_ID` |

