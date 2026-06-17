# OMF_EXPRESS_DICTIONARY

> Holds the list of all values which can be checked in calc engine rules.

**Description:** OMF EXPRESS DICTIONARY  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ARRAY_STR` | VARCHAR(255) |  |  | String used to qualify arrays for rules. |
| 3 | `CCL_STRING` | VARCHAR(255) |  |  | The CCL code that is used in the formulas created by the OMF rule building applications. |
| 4 | `DETAIL_IND` | DOUBLE |  |  | Indicates whether the data is at the detail level (=1) - such as verifying tech, detail procedure, performing tech - or at the order level or higher (=0) - such as admitting physician, encntr_type, order_date, and patient. |
| 5 | `DISPLAY_ORDER` | DOUBLE |  |  | Order to display qualifications in the (IC) Rule builder. |
| 6 | `EXPRESS_CD` | DOUBLE |  |  | The code value that indicates whether the expression is used for rule qualification, calculation, or both. |
| 7 | `EXPRESS_NUM` | DOUBLE | NOT NULL |  | Unique identification number for the expression. |
| 8 | `EXPRESS_SEQ` | DOUBLE | NOT NULL |  | Sequence number used to order 'ccl_string's if they are greater than 255. Also provides uniqueness when this happens. |
| 9 | `FILTER_MEANING` | VARCHAR(50) |  |  | Name of filter from the omf_filter_meaning table. Is used to get the list of values for the TAT tool. |
| 10 | `GROUP_NUM` | DOUBLE |  |  | Groups express ids by purpose. |
| 11 | `MODE_CD` | DOUBLE |  |  | The code_value for the rule mode (only used in Infection Control. Examples: susceptibilities, antibiotics, and general lab results). Code set 14199. |
| 12 | `MULTIPLE_IND` | DOUBLE |  |  | Can multiple values be selected for this condition? |
| 13 | `OMF_GROUPING_CD` | DOUBLE |  |  | No longer used. |
| 14 | `PL_SQL_FUNCTION` | VARCHAR(255) |  |  | PL/SQL function to be applied to the CCL string outside of the normal select statement. Is a temporary work around until we can apply PL/SQL functions around CCL functions. |
| 15 | `PRODUCT_CD` | DOUBLE | NOT NULL |  | The code_value which identifies the product (e.g. Infection Control or Service Management). Code set 14135. |
| 16 | `PROSE` | VARCHAR(255) |  |  | Free text long description of the expression. |
| 17 | `REQUIRED_IND` | DOUBLE |  |  | Is this condition required? For example, in any IC susceptibility rule an antibiotic must be listed while source, isolate, and result do not. |
| 18 | `REQ_GROUP_NUM` | DOUBLE |  |  | The express_id of a group of this id. In the (IC) rule builder this will allow the user to only use a group OR the individual members but not both. |
| 19 | `SHOW_ALL_IND` | DOUBLE |  |  | OBSOLETE - Get from Filter meaning now. Used inTAT tool. 0 = Search prompt. Partial list appears; 1 = No search prompt. Entire list appear |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 25 | `XREF_SCRIPT_NBR` | DOUBLE |  |  | OBSOLETE - Get from Filter meaning now. Script request number which will produce the list of values to be displayed. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

