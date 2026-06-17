# CONVERT_AUDIT_TRANSACTION

> Stores audit transactions for order conversion. An audit transaction describes all request information during a single transaction for a consumer.

**Description:** Convert Audit Transaction  
**Table type:** ACTIVITY  
**Primary key:** `CONVERT_AUDIT_TRANSACTION_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONVERT_AUDIT_TRANSACTION_ID` | DOUBLE | NOT NULL | PK | The unique primary key of this table. It is an internally generated sequence number. |
| 2 | `FACILITY_CD` | DOUBLE | NOT NULL |  | The facility in which the conversion is taking place. |
| 3 | `PHARMACY_TYPE_BIT` | DOUBLE | NOT NULL |  | The bitmask defining the pharmacy types requested. |
| 4 | `PPR_CD` | DOUBLE | NOT NULL |  | The patient-provider relationship of the personnel performing the conversion, if one exists. |
| 5 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the personnel performing the conversion. |
| 6 | `RETRIEVE_NO_RX_MASK_IND` | DOUBLE | NOT NULL |  | Indicates that synonyms with no pharmacy type were requested. |
| 7 | `RETRIEVE_PRODUCTS_ONLY_IND` | DOUBLE | NOT NULL |  | Indicates that only product synonyms should be retrieved. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VENUE_FLAG` | DOUBLE | NOT NULL |  | The venue to which the order is being converted. 1 - Prescription, 2 - Inpatient |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CONVERT_AUDIT_SYNONYM](CONVERT_AUDIT_SYNONYM.md) | `CONVERT_AUDIT_TRANSACTION_ID` |

