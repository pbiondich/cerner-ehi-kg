# LH_RULES

> This table is used to store the rules that calculate the measures of Lighthouse topics.

**Description:** LH_RULES  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL |  | ID relating to the Lighthouse Topic (FALLS, HAPU, SSI, etc.) Foreign Key to BR_DATAMART_CATEGORY |
| 4 | `BR_DATAMART_FILTER_ID` | DOUBLE | NOT NULL |  | ID relating to the user-configurable filters Foreign Key to BR_DATAMART_FILTER |
| 5 | `CATEGORY_MEAN` | VARCHAR(30) |  |  | Unique string to identify the category from BR_DATAMART_CATEGORY |
| 6 | `CHILD_LH_RULES_ID` | DOUBLE | NOT NULL |  | The rules_id that this rule is linked to |
| 7 | `CUSTOM_RULE_IND` | DOUBLE |  |  | Identifies rules that are not loaded from the standard Lighthouse Rules definitions |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 10 | `FILTER_MEAN` | VARCHAR(255) |  |  | String that identifies the filter from BR_DATAMART_FILTER |
| 11 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 12 | `LH_RULES_ID` | DOUBLE | NOT NULL |  | Unique identifier for the rule. |
| 13 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 14 | `MEASURE_DESC` | VARCHAR(50) |  |  | Description of the Measure (AT_RISK, ASSESSED_DAILY, etc.) for the Lighthouse Topic |
| 15 | `OPERATION` | VARCHAR(25) |  |  | If this rule is linked to another rule, this is the operation that is performed to link them (AND, OR, etc.) |
| 16 | `PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was loaded into the table. |
| 17 | `REQUIRED_IND` | DOUBLE |  |  | Shows if this rule is required or optional |
| 18 | `RULES_SEQ` | DOUBLE |  |  | The sequence a group of rules are put together |
| 19 | `RULE_TXT` | VARCHAR(255) |  |  | The rule being applied to calculate the measure |
| 20 | `SUB_RULE_IND` | DOUBLE |  |  | Indicates if the rule field points to a sub-rule or if the rule field contains the text of the rule. |
| 21 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 24 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

