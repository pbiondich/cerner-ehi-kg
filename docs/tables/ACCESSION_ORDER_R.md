# ACCESSION_ORDER_R

> The resolution table between accessions and orders. This table will tell you what orders belong to an accession. It will also tell you what accession(s) an order belongs to.

**Description:** Accession/Order relationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(20) |  |  | An accession uniquely identifies a specimen. |
| 2 | `ACCESSION_ID` | DOUBLE | NOT NULL |  | A system generated number that uniquely identifies an accession number. |
| 3 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | A code value that uniquely identifies to which "net" (such as PathNet or RadNet) and/or what department (such as General Lab or Microbiology) an order belongs. |
| 4 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | A system generated number that uniquely identifies an order. |
| 5 | `PRIMARY_FLAG` | DOUBLE | NOT NULL |  | Determines if this is the primary accession for the order.0 - This is the primary accession for the order.1 - This is the secondary accession for the order. This is the original accession that was created for the order but replaced due to a missed collection and reshcedule of the order. |
| 6 | `PRIMARY_IND` | DOUBLE |  |  | This field identifies which accession is the current, primary indicator for a particular order. The field should be set to 1 if the accession on this row is the current primary accession for the order on this row, otherwise it should be set to 0. This field will be used for future functionality. |
| 7 | `RESTRICT_AV_IND` | DOUBLE | NOT NULL |  | The restrict autoverification indicator is set from the AVStatus.dll and indicates when the accession is restricted from being autoverified. A value of 1 indicates the accession is restricted from being autoverified. A value of 0 indicates the accession is not restricted from being autoverified. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

