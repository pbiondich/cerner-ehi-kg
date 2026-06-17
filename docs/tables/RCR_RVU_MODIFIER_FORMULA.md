# RCR_RVU_MODIFIER_FORMULA

> This table defines the formula to use when calculating the RVU value for each modifier.

**Description:** Revenue Cycle Reporting RVU Modifier Formula  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | The Billing Entity for which the modifier formula is built. |
| 4 | `CALCULATION_VALUE` | DOUBLE | NOT NULL |  | The value by which the specific Modifier will alter the RVU |
| 5 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Contains the record creation date. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `GLOBAL_IND` | DOUBLE | NOT NULL |  | Indicates if the calculation value will be applied individually or to the entire RVU. |
| 8 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 9 | `MODIFIER_IDENT` | VARCHAR(50) |  |  | Identifies the Modifier for which the formula applies. |
| 10 | `MODIFIER_POSITION_NBR` | DOUBLE | NOT NULL |  | The position of the modifier assignment (e.g. Primary, Secondary, etc.) |
| 11 | `PERCENTAGE_IND` | DOUBLE | NOT NULL |  | Indicates if the calculation value is a percent or normal number. |
| 12 | `RCR_RVU_MODIFIER_FORMULA_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RCR_RVU_MODIFIER_FORMULA table. |
| 13 | `RVU_OVERRIDE_IND` | DOUBLE | NOT NULL |  | This is set to True if the modifier within the RVU formula will override the RVU value to be 0.0 rather than the calculated value. |
| 14 | `SOURCE_VOCABULARY_CD` | DOUBLE | NOT NULL |  | The source vocabulary for which the modifier formula is built (e.g. CPT4, HCPCS) |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

