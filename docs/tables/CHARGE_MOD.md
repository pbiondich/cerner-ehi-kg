# CHARGE_MOD

> Suspense reasons and bill codes for processed charge events. Charge_mod_type_cd defines the type of modification.

**Description:** Charge Modifier  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 34

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_DT_TM` | DATETIME |  |  | not used |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CHARGE_ITEM_ID` | DOUBLE | NOT NULL | FK→ | ID from the charge table for the charge this mod is associated with. |
| 8 | `CHARGE_MOD_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the charge_mod table. It is an internal system assigned number. |
| 9 | `CHARGE_MOD_SOURCE_CD` | DOUBLE |  |  | This column specifies where the charge modification came from: upstream, reference build or modified manually. |
| 10 | `CHARGE_MOD_TYPE_CD` | DOUBLE | NOT NULL |  | Value from 13019 that represents the type of modification this row is such as bill code or suspense. |
| 11 | `CM1_NBR` | DOUBLE | NOT NULL |  | Generic field to store floating point data. When charge_mode_type_cd is the code value for 'BILL_CODE' from code_set 13019 and field1_id is the code value for "HCPCS' from code_set 14002 this field will store the QCF (Quantity Conversion Factor) value. |
| 12 | `CODE1_CD` | DOUBLE | NOT NULL |  | reserved for future use. Depending on the value in charge_mod_type_cd, this is either the value from 13030 that represents the suspense reason, or it is the value from 14002 that represents the bill code schedule. |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `FIELD1` | VARCHAR(200) |  |  | No longer used. Depending on the value in charge_mod_type_cd, this is either the value from 13030 that represents the suspense reason, or it is the value from 14002 that represents the bill code schedule. |
| 15 | `FIELD10` | VARCHAR(200) |  |  | not used |
| 16 | `FIELD1_ID` | DOUBLE | NOT NULL |  | Depending on the value in charge_mod_type_cd, this is either the value from 13030 that represents the suspense reason, or it is the value from 14002 that represents the bill code schedule. |
| 17 | `FIELD2` | VARCHAR(200) |  |  | Depending on the value in charge_mod_type_cd, this is either the suspense description, or it is the bill code that has been assigned (in the case of ICD9 bill codes, this is the source_identifier from the nomenclature table). |
| 18 | `FIELD2_ID` | DOUBLE | NOT NULL |  | Priority on bill codes or sequence on the suspense reason. |
| 19 | `FIELD3` | VARCHAR(350) |  |  | Depending on the value of charge_mod_type_cd, this is either a counter of suspense reasons for the charge_item_id starting with zero, or it is the bill code description (in the case of ICD9 bill ocdes, this is the source_string from nomenclature table). |
| 20 | `FIELD3_ID` | DOUBLE | NOT NULL |  | Nomenclature ID on ICD9 bill codes. |
| 21 | `FIELD4` | VARCHAR(200) |  |  | If the charge_mod_type_cd represents bill code, this is the priority for multiple bill codes assigned to the same charge_item_id, otherwise it is null. |
| 22 | `FIELD4_ID` | DOUBLE | NOT NULL |  | not used |
| 23 | `FIELD5` | VARCHAR(200) |  |  | reserved for future use. If the charge_mod_type_cd represents bill code of type ICD9, this is the nomenclature_id for the diagnosis code. |
| 24 | `FIELD5_ID` | DOUBLE | NOT NULL |  | not used |
| 25 | `FIELD6` | VARCHAR(200) |  |  | not used |
| 26 | `FIELD7` | VARCHAR(200) |  |  | not used |
| 27 | `FIELD8` | VARCHAR(200) |  |  | not used |
| 28 | `FIELD9` | VARCHAR(200) |  |  | not used |
| 29 | `NOMEN_ID` | DOUBLE | NOT NULL |  | This is the unique primary identifier from the nomenclature table for a corresponding bill code. It is mostly used for Charge Transformation. |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHARGE_ITEM_ID` | [CHARGE](CHARGE.md) | `CHARGE_ITEM_ID` |

