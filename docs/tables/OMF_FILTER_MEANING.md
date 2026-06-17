# OMF_FILTER_MEANING

> Info about column 'types' such as physician id (whether ordering, discharge, etc), tech id, date, etc.

**Description:** Info about column 'types' such as physician id (whether ordering, discharge, etc  
**Table type:** REFERENCE  
**Primary key:** `FILTER_MEANING`  
**Columns:** 20  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CORE_IND` | DOUBLE | NOT NULL |  | Indicates this row was created by Cerner. |
| 3 | `DESCRIPTION` | VARCHAR(255) |  |  | Filter meaning description. |
| 4 | `DISPLAY_FUNCTION` | VARCHAR(100) |  |  | Function needed to display a stored code value or id. |
| 5 | `FILTER_MEANING` | VARCHAR(50) | NOT NULL | PK | Name of the filter meaning. |
| 6 | `FILTER_PE_NAME` | VARCHAR(40) |  |  | Parent entity name of this meaning. E.g. 'Code_value', 'Person', etc. This will be stamped on tables (such as omf_pv_security_filter and omf_pvi_filter) which will generically store these values. This is done so merges of these tables will be successful. |
| 7 | `FILTER_SCRIPT` | DOUBLE |  |  | Script to get list of possible items. |
| 8 | `INACTIVE_PROMPT_IND` | DOUBLE |  |  | Tells PowerVision whether the filtering dialog should display a prompt asking the user if they want to see inactive rows. |
| 9 | `OWNER_GROUP_CD` | DOUBLE | NOT NULL |  | The owner group of the filter meaning, used to categorize items across a solution group or functional area (ex Operational vs Financial). |
| 10 | `SHOW_ALL_IND` | DOUBLE |  |  | Whether all values will be displayed at once or if a start value should be prompted for. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `VAL1` | VARCHAR(255) |  |  | Passed in string value 1 to filter scripts. Typically will be the filter program name. |
| 17 | `VAL2` | VARCHAR(255) |  |  | Passed in string value 2 to filter scripts. Typically a parameter such as code set or cdf_meaning. |
| 18 | `VAL3` | VARCHAR(255) |  |  | Passed in string value 3 to filter scripts. Typically a parameter such as code set or cdf_meaning. |
| 19 | `VAL4` | VARCHAR(255) |  |  | Passed in string value 4 to filter scripts. Typically a parameter such as code set or cdf_meaning. |
| 20 | `VAL5` | VARCHAR(255) |  |  | Passed in string value 5 to filter scripts. Typically a parameter such as code set or cdf_meaning. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [DA_ELEMENT](DA_ELEMENT.md) | `FILTER_MEANING` |
| [OMF_AUTH_ATTR](OMF_AUTH_ATTR.md) | `FILTER_MEANING` |
| [OMF_CFGRN_ITEM](OMF_CFGRN_ITEM.md) | `FILTER_MEANING` |

