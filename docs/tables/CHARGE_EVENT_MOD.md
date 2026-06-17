# CHARGE_EVENT_MOD

> Contains ICD-9 codes that are entered at order entry time.

**Description:** Charge Event Modification  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 33

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_DT_TM` | DATETIME |  |  | Stores the activity date and time for the charge event modifier, primarily used for FLEX fields which are date inputs. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CHARGE_EVENT_ID` | DOUBLE | NOT NULL | FK→ | ID from the charge_event table for the charge_event this mod is associated with. |
| 8 | `CHARGE_EVENT_MOD_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the charge_event_mod table. It is an internal system assigned number. |
| 9 | `CHARGE_EVENT_MOD_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates what type of mod this is, such as BILL CODE for ICD9. |
| 10 | `CM1_NBR` | DOUBLE | NOT NULL |  | Generic field to store floating point data. When charge_event_mod_type_cd is the code value for "BILL CODE" from code_set 13019 and field1_id is the code value for "HCPCS" from code_set 14002 this field will store the QCF (Quantity Conversion Factor) value. |
| 11 | `CODE1_CD` | DOUBLE | NOT NULL |  | not used |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `FIELD1` | VARCHAR(200) |  |  | Code value from 14002 that indicates this is an ICD9. |
| 14 | `FIELD10` | VARCHAR(200) |  |  | not used |
| 15 | `FIELD1_ID` | DOUBLE | NOT NULL |  | Code value from 14002 that indicates this is an ICD9. |
| 16 | `FIELD2` | VARCHAR(200) |  |  | Source identifier from nomenclature table. |
| 17 | `FIELD2_ID` | DOUBLE | NOT NULL |  | Priority. |
| 18 | `FIELD3` | VARCHAR(200) |  |  | Source string from nomenclature table. |
| 19 | `FIELD3_ID` | DOUBLE | NOT NULL |  | Nomenclature identifier. |
| 20 | `FIELD4` | VARCHAR(200) |  |  | Priority. This will continue to be populated until schema change has been rolled out to all sites. |
| 21 | `FIELD4_ID` | DOUBLE | NOT NULL |  | not used. |
| 22 | `FIELD5` | VARCHAR(200) |  |  | Nomenclature id. This will continue to be populated until the schema change has been rolled out to all sites. |
| 23 | `FIELD5_ID` | DOUBLE | NOT NULL |  | not used |
| 24 | `FIELD6` | VARCHAR(200) |  |  | not used |
| 25 | `FIELD7` | VARCHAR(200) |  |  | not used |
| 26 | `FIELD8` | VARCHAR(200) |  |  | not used |
| 27 | `FIELD9` | VARCHAR(200) |  |  | not used |
| 28 | `NOMEN_ID` | DOUBLE | NOT NULL |  | not used |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHARGE_EVENT_ID` | [CHARGE_EVENT](CHARGE_EVENT.md) | `CHARGE_EVENT_ID` |

