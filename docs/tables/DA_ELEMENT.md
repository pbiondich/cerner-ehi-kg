# DA_ELEMENT

> Defines a column of information that may be used in a query and/or used to filter a query. The element may contain an sql select, a where clause, as well as the defining qualities of the element that are needed by the Discern Analytics 2.0 reporting system.qualities of the element that are needed by the reporting system.

**Description:** Discern Analytics Element  
**Table type:** REFERENCE  
**Primary key:** `DA_ELEMENT_ID`  
**Columns:** 34  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AGGREGATE_FN_CD` | DOUBLE | NOT NULL |  | Code value which identifies the aggregate function to use with this element in the data cube. |
| 3 | `COLUMN_STRING_TXT_ID` | DOUBLE | NOT NULL | FK→ | Reference to the long_text_reference table which contains the expression which represents how the data item will be retrieved by a query. |
| 4 | `COLUMN_VAL_FLAG` | DOUBLE | NOT NULL |  | Indicates which attribute, if any, defines the element's ID value. Useful when the column select clause is display text. |
| 5 | `CORE_IND` | DOUBLE | NOT NULL |  | Indicates this row was created by Cerner. |
| 6 | `DA_ELEMENT_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the DA_ELEMENT table. |
| 7 | `DEPRECATED_IND` | DOUBLE | NOT NULL |  | Indicates this element has been deprecated. A row that has been deprecated indicates that there is a future intention to inactivate the row. |
| 8 | `ELEMENT_DESC` | VARCHAR(255) | NOT NULL |  | A description of how the element is displayed or used. |
| 9 | `ELEMENT_NAME` | VARCHAR(100) | NOT NULL |  | The unique name for the Element. |
| 10 | `ELEMENT_NAME_KEY` | VARCHAR(100) | NOT NULL |  | Uppercased element_name with white spaces and special characters removed. |
| 11 | `ELEMENT_NAME_KEY_A_NLS` | VARCHAR(400) |  |  | The NLS key for searching in all non-English locales. |
| 12 | `ELEMENT_TYPE_CD` | DOUBLE | NOT NULL |  | Code value that Defines the type of element, such as fact or dimension. |
| 13 | `ELEMENT_UUID` | VARCHAR(100) | NOT NULL |  | The UUID is used to establish a unique identifier across all systems. The UUID for an item will be the same from one environment to another. |
| 14 | `FILTER_CODE_SET` | DOUBLE | NOT NULL |  | Code set used for generic code value filters. |
| 15 | `FILTER_IND` | DOUBLE | NOT NULL |  | Specifies whether the element is filterable. |
| 16 | `FILTER_MEANING` | VARCHAR(50) | NOT NULL | FK→ | Reference to the filter meaning table. The filter meaning retrieves the information used for displaying prompts and filters. |
| 17 | `FORMAT_TXT` | VARCHAR(50) | NOT NULL |  | Optionally specifies how the element is formatted for reporting. |
| 18 | `GROUP_BY_COLUMN_IND` | DOUBLE | NOT NULL |  | Indicates if the SQL engine will include the text contained in the column_string_txt_id from the long_text_reference in the group by clause. |
| 19 | `GROUP_BY_IND` | DOUBLE | NOT NULL |  | Specifies whether the group_by_string_txt will be added to the Group By . |
| 20 | `GROUP_BY_QUAL_IND` | DOUBLE | NOT NULL |  | Indicates whether the qualification string text will be included in the group by statement. |
| 21 | `GROUP_BY_STRING_TXT` | VARCHAR(255) |  |  | Alternate value to be used in group by expression. |
| 22 | `KEY_ELEMENT_ID` | DOUBLE | NOT NULL | FK→ | Reserved for future use. |
| 23 | `OWNER_GROUP_CD` | DOUBLE | NOT NULL |  | The owner group of the element, used to categorize items across a solution group |
| 24 | `QUAL_DATA_TYPE_FLAG` | DOUBLE | NOT NULL |  | Specifies the data type returned for the qualification such as date, numeric, string |
| 25 | `QUAL_STRING_TXT` | VARCHAR(255) |  |  | Represents the SQL string that will be used in the where clause when this element is used as a filter. |
| 26 | `RESULT_DATA_TYPE_FLAG` | DOUBLE | NOT NULL |  | Specifies the data type returned for the result such as date, numeric, string. |
| 27 | `SORT_FLAG` | DOUBLE | NOT NULL |  | Specifies the report type of sorting used for this element. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 33 | `VERSION_TXT` | VARCHAR(50) | NOT NULL |  | Version_txt contains both a major and minor version number. Minor version numbers are auto-updated each time the item is updated, whereas the major version may be updated during the export process. The version_txt is used by the import process to ensure accurate updating across systems. |
| 34 | `WHERE_CLAUSE_TXT_ID` | DOUBLE | NOT NULL | FK→ | Reference to the long_text_reference table which contains an qualification expression for the element. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COLUMN_STRING_TXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `FILTER_MEANING` | [OMF_FILTER_MEANING](OMF_FILTER_MEANING.md) | `FILTER_MEANING` |
| `KEY_ELEMENT_ID` | [DA_ELEMENT](DA_ELEMENT.md) | `DA_ELEMENT_ID` |
| `WHERE_CLAUSE_TXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [DA_BV_LV_ELEM_RELTN](DA_BV_LV_ELEM_RELTN.md) | `DA_ELEMENT_ID` |
| [DA_CALC_ELEM_RELTN](DA_CALC_ELEM_RELTN.md) | `CHILD_ELEMENT_ID` |
| [DA_CALC_ELEM_RELTN](DA_CALC_ELEM_RELTN.md) | `PARENT_ELEMENT_ID` |
| [DA_ELEMENT](DA_ELEMENT.md) | `KEY_ELEMENT_ID` |
| [DA_ELEM_UDF_RELTN](DA_ELEM_UDF_RELTN.md) | `DA_ELEMENT_ID` |
| [DA_LV_TABLE_ELEM_RELTN](DA_LV_TABLE_ELEM_RELTN.md) | `DA_ELEMENT_ID` |

