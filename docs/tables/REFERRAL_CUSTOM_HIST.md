# REFERRAL_CUSTOM_HIST

> Stores the history of all the custom field values attributed for a referral

**Description:** Referral Custom History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME |  |  | Dzte and time the referral was created |
| 2 | `REFERRAL_CUSTOM_FIELD_KEY` | VARCHAR(255) |  |  | Identifies a unique custom field name for the specific referral. |
| 3 | `REFERRAL_CUSTOM_HIST_ID` | DOUBLE | NOT NULL |  | A system generated code used to uniquely identify a row on the REFERRAL_CUSTOM_HIST table. |
| 4 | `REFERRAL_CUSTOM_ID` | DOUBLE |  | FK→ | PRIMARY KEY |
| 5 | `REFERRAL_CUSTOM_VALUE_BOOLEAN` | DOUBLE |  |  | Contains the boolean value associated to the custom field defined in referral_custom_field_key. |
| 6 | `REFERRAL_CUSTOM_VALUE_DOUBLE` | DOUBLE |  |  | Contains the double value associated to the custom field defined in referral_custom_field_key. |
| 7 | `REFERRAL_CUSTOM_VALUE_DT_TM` | DATETIME |  |  | Contains the date/time value associated to the custom field defined in referral_custom_field_key. |
| 8 | `REFERRAL_CUSTOM_VALUE_STRING` | VARCHAR(255) |  |  | Contains the string value associated to the custom field defined in referral_custom_field_key. |
| 9 | `REFERRAL_CUSTOM_VALUE_TYPE` | VARCHAR(40) |  |  | Identifies the data type of the value corresponding to the custom key defined in referral_custom_field_key. This will indicate the referral_custom_value_* column that is populated. |
| 10 | `REFERRAL_ID` | DOUBLE |  | FK→ | A foreign key value from the REFERRAL table which Uniquely identifies the related referral. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REFERRAL_CUSTOM_ID` | [REFERRAL_CUSTOM](REFERRAL_CUSTOM.md) | `REFERRAL_CUSTOM_ID` |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | `REFERRAL_ID` |

