# PCS_KIT_DEFINITION

> This table stores the static definition information for a PathNet kit.

**Description:** PathNet Common Services Kit Definition  
**Table type:** ACTIVITY  
**Primary key:** `KIT_DEFINITION_ID`  
**Columns:** 13  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | This field allows the kit definitions to be grouped and filtered by the type of activity the kit will be used for (i.e. Microbiology, Blood Bank, etc.) |
| 2 | `AVAILABLE_IND` | DOUBLE | NOT NULL |  | This field indicates when a kit definition is ready to be put into use for patient results. |
| 3 | `COMMENT_TEXT_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the LONG_TEXT row that contains the kit definition comment text. |
| 4 | `CROSS_COMPONENT_LOT_IND` | DOUBLE | NOT NULL |  | This field indicates whether or not a component lot of the kit can be used outside of the kit. |
| 5 | `KIT_DEFINITION_ID` | DOUBLE | NOT NULL | PK | This field contains the unique value that identifies a kit definition. |
| 6 | `KIT_DEFINITION_NAME` | CHAR(40) | NOT NULL |  | This field contains the user-defined name for the kit definition. |
| 7 | `MANUFACTURER_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the manufacturer associated with the kit definition. |
| 8 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the service resource associated with the kit definition. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PCS_KIT_INFORMATION](PCS_KIT_INFORMATION.md) | `KIT_DEFINITION_ID` |
| [PCS_LOT_DEFINITION](PCS_LOT_DEFINITION.md) | `KIT_DEFINITION_ID` |

