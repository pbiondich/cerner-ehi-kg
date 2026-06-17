# CT_RULE_DETAIL

> Charge Transformation Rule Detail table

**Description:** This table holds all the rule details for a particular rule.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `COUNT_BEG` | DOUBLE |  |  | The beginning count number. |
| 7 | `COUNT_END` | DOUBLE |  |  | The ending count number. |
| 8 | `CT_RULE_DETAIL_ID` | DOUBLE | NOT NULL |  | This is the unique primary identifier for the ct_rule_detail table. It is an internal assigned system number. |
| 9 | `CT_RULE_ID` | DOUBLE | NOT NULL |  | This the unique primary identifier for the ct_rule table. |
| 10 | `DETAIL_TYPE_CD` | DOUBLE | NOT NULL |  | Value from 15729 that indicates whether or not a charge is a PRECURSOR or RESULT. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `OPERATOR_CD` | DOUBLE | NOT NULL |  | Value from 18849 that indicates either multiply, subtract, equal, add, and or or. |
| 13 | `PRECEDENCE` | DOUBLE |  |  | Indicates the priority of the rule detail. |
| 14 | `RESULT_FACTOR` | DOUBLE |  |  | Holds the value for the REPLACEPRICE or the REPLACEADJUST. |
| 15 | `RULE_ENTITY_ID` | DOUBLE | NOT NULL |  | Depending on the rule_entity_name, this field either holds the nomen_id from the nomenclature table for a particular orderable, or the bill_item_id from the bill_item table.. |
| 16 | `RULE_ENTITY_NAME` | VARCHAR(32) |  |  | Either NOMENCLATURE or BILLITEM. |
| 17 | `SEQUENCE` | DOUBLE |  |  | The order by which the NOMENCLATURE or BILLITEM types were entered. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

