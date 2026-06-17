# BT_FIELD_RELTN

> Bill Template Field Relation

**Description:** Bill Template Field Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ATTRIB_FIELD_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Attribute Field Relation ID |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BILL_TEMPL_ID` | DOUBLE | NOT NULL | FK→ | This column relates this record to a specific Bill Template. |
| 8 | `BT_FIELD_RELTN_ID` | DOUBLE | NOT NULL |  | Bill Template Field Relation ID |
| 9 | `BT_FIELD_VRSN_NBR` | DOUBLE | NOT NULL |  | Bill Template Field Version Number |
| 10 | `CUSTOM_IND` | DOUBLE |  |  | Custom Indicator |
| 11 | `DATA_TYPE_CD` | DOUBLE | NOT NULL |  | Data Type Code value |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `FLD_JUSTIFICATION_CD` | DOUBLE | NOT NULL |  | Field Justification Code |
| 14 | `MAX_FIELD_LENGTH` | DOUBLE |  |  | Maximum Field Length |
| 15 | `MIN_FIELD_LENGTH` | DOUBLE |  |  | Minimum Field Length |
| 16 | `PATTERN_CHK_IND` | DOUBLE |  |  | Pattern Check Indicator |
| 17 | `REQUIRED_IND` | DOUBLE |  |  | Required Indicator |
| 18 | `UDV_ID` | DOUBLE | NOT NULL | FK→ | User-Defined Value ID - Not Used |
| 19 | `UDV_TEXT` | VARCHAR(250) |  |  | User Defined Value Text |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 25 | `USER_DEFINED_IND` | DOUBLE |  |  | User-Defined Indicator - Not Used |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ATTRIB_FIELD_RELTN_ID` | [ATTRIB_FIELD_RELTN](ATTRIB_FIELD_RELTN.md) | `ATTRIB_FIELD_RELTN_ID` |
| `BILL_TEMPL_ID` | [BILL_TEMPL](BILL_TEMPL.md) | `BILL_TEMPL_ID` |
| `UDV_ID` | [USER_DEFINED_VALUE](USER_DEFINED_VALUE.md) | `UDV_ID` |

