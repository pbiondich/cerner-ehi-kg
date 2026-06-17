# CONTENT_PROPERTY

> Content Property Table

**Description:** Content Property  
**Table type:** REFERENCE  
**Primary key:** `PROPERTY_ID`  
**Columns:** 20  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHAR_LEN` | DOUBLE |  |  | The character length for the content property |
| 2 | `CSV_TEMPLATE_HELP` | VARCHAR(1000) |  |  | Help text used for the CSV converter templates. This will be an explanation of how to locate and/or provide a value that will be valid in contentmanager after the csv file is converted. |
| 3 | `DEFAULT_VALUE` | VARCHAR(255) |  |  | The default value for the property |
| 4 | `DISPLAY` | VARCHAR(100) |  |  | Display for the content property |
| 5 | `DOMAIN_NAME` | VARCHAR(100) |  |  | The domain where this property belongs |
| 6 | `LIST_IND` | DOUBLE |  |  | List IndicatorColumn |
| 7 | `PICK_FROM_LIST_IND` | DOUBLE |  |  | Used to determine whether the application should limit the selection from the list only or should allow free-text. |
| 8 | `PROPERTY_HELP_LIST` | VARCHAR(1000) |  |  | Stores the user defined help as XML string. |
| 9 | `PROPERTY_ID` | DOUBLE | NOT NULL | PK | Property IdentifierColumn |
| 10 | `PROPERTY_LOCK_TYPE` | DOUBLE |  |  | Used to determine how a content property behaves, such as locked or unlocked. |
| 11 | `PROPERTY_TYPE` | DOUBLE |  |  | Identifies the data type for the content property |
| 12 | `PROPERTY_UPDATE_FLAG` | DOUBLE | NOT NULL |  | Identifies whether the field is selected to update (0), not update (1), or rely on business logic script (2). |
| 13 | `PROPERTY_VALIDATED_BY` | DOUBLE |  |  | Identifies the type of validation if the property is a code set |
| 14 | `REQUIRED_IND` | DOUBLE |  |  | Whether the property is required or not. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 20 | `XML_DISPLAY` | VARCHAR(100) |  |  | xml tag for the content property |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (5)

| From table | Column |
|------------|--------|
| [COND_REQUIRED_PROPS](COND_REQUIRED_PROPS.md) | `COND_PROPERTY_ID` |
| [COND_REQUIRED_PROPS](COND_REQUIRED_PROPS.md) | `PROPERTY_ID` |
| [CONTENT_PROPERTY_MAP](CONTENT_PROPERTY_MAP.md) | `CONTENT_PROPERTY_ID` |
| [CONTENT_PROPERTY_RELTN](CONTENT_PROPERTY_RELTN.md) | `CHILD_PROPERTY_ID` |
| [CONTENT_PROPERTY_RELTN](CONTENT_PROPERTY_RELTN.md) | `PARENT_PROPERTY_ID` |

