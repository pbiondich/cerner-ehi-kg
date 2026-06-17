# CP_COMPONENT_DETAIL

> Contain detailed configuration information for a care planning component

**Description:** Care Planning Component Detail  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLLATION_SEQ` | DOUBLE | NOT NULL |  | This column is used to order all the items in the table. |
| 2 | `COMPONENT_DETAIL_RELTN_CD` | DOUBLE | NOT NULL |  | Code Value identifying component relationship detail |
| 3 | `COMPONENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Contains the PK value of a row in table idenitified in COMPONENT_ENTITY_NAME. If COMPONENT is not related to a table/value, then this value is 0 |
| 4 | `COMPONENT_ENTITY_NAME` | VARCHAR(30) |  |  | Contains name of table if the COMPONENT ENTITY is related to a table |
| 5 | `COMPONENT_IDENT` | VARCHAR(255) |  |  | Identifier for COMPONENT DETAIL - only used when COMPONENT_ENTITY_ID = 0 |
| 6 | `COMPONENT_TEXT` | VARCHAR(255) |  |  | Detail text associated with the named detail. Contains a value when COMPONENT_IDENT is used and COMPONENT_ENTITY_ID = 0 |
| 7 | `CP_COMPONENT_DETAIL_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 8 | `CP_COMPONENT_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to Component this detail config is associated to |
| 9 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | The latest row that will default the build tool |
| 10 | `SELECTED_IND` | DOUBLE | NOT NULL |  | This field is used to determine if an item should be pre-selected when the page loads. |
| 11 | `SOURCE_FLAG` | DOUBLE | NOT NULL |  | The source of the component detail for documentation content |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `VERSION_FLAG` | DOUBLE | NOT NULL |  | The Version Flag will control the severity of versioning changes for the detail |
| 18 | `VERSION_NBR` | DOUBLE | NOT NULL |  | Version is controlled by outside source and intended to match up with DD_SREF_TEMPLATE.VERSION_NBR |
| 19 | `VERSION_TEXT` | VARCHAR(255) |  |  | Text that will show the user what content changes have occurred |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CP_COMPONENT_ID` | [CP_COMPONENT](CP_COMPONENT.md) | `CP_COMPONENT_ID` |

